import os
from collections.abc import AsyncIterable, AsyncIterator

import pytest
from dishka import AsyncContainer, Provider, Scope, make_async_container
from fastapi import FastAPI
from faststream.confluent import KafkaBroker, TestKafkaBroker
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine

from applications.bootstrap.configs import load_configs
from applications.bootstrap.ioc import (
    adapters_provider,
    db_provider,
    interactors_provider,
    services_provider,
)
from applications.infrastructure.broker.publisher import AppTopic
from applications.infrastructure.configs import (
    APIConfig,
    KafkaConfig,
    PostgresConfig,
)
from applications.infrastructure.persistence.models.base import metadata
from applications.web import create_app


def _load_env() -> None:
    os.environ["POSTGRES_USER"] = "postgres"
    os.environ["POSTGRES_PASSWORD"] = "postgres"  # noqa: S105
    os.environ["POSTGRES_HOST"] = "localhost"
    os.environ["POSTGRES_PORT"] = "5432"
    os.environ["POSTGRES_DB"] = "test"
    os.environ["POSTGRES_DEBUG"] = "true"
    os.environ["UVICORN_HOST"] = "127.0.0.1"
    os.environ["UVICORN_PORT"] = "8888"


async def test_broker() -> AsyncIterable[KafkaBroker]:
    broker = KafkaBroker(KafkaConfig("127.0.0.1", "9092").uri)
    async with TestKafkaBroker(broker) as br:
        yield br


def _test_container() -> AsyncContainer:
    configs = load_configs()
    test_provider = Provider(scope=Scope.APP)
    test_provider.provide(lambda: AppTopic("Test"), provides=AppTopic)
    test_provider.provide(lambda: configs.postgres, provides=PostgresConfig)
    test_provider.provide(lambda: configs.web, provides=APIConfig)
    test_provider.provide(lambda: configs.kafka, provides=KafkaConfig)
    test_provider.provide(test_broker)
    return make_async_container(
        test_provider,
        db_provider(),
        adapters_provider(),
        interactors_provider(),
        services_provider(),
    )


@pytest.fixture(scope="session")
async def app() -> AsyncIterator[FastAPI]:
    _load_env()
    container = _test_container()
    app = create_app()
    app.state.dishka_container = container
    engine = await container.get(AsyncEngine)

    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

    yield app

    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)


@pytest.fixture(scope="session")
async def client(app: FastAPI) -> AsyncIterator[AsyncClient]:
    t = ASGITransport(app)
    async with AsyncClient(transport=t, base_url="http://test") as ac:
        yield ac
