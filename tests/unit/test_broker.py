from collections.abc import AsyncIterable
from unittest import mock

import pytest
from faststream.confluent import KafkaBroker, TestKafkaBroker

from applications.entities.application.services import ApplicationService
from applications.infrastructure.broker.provider import get_broker
from applications.infrastructure.broker.publisher import (
    ApplicationPublisherKafka,
    AppTopic,
)
from applications.infrastructure.configs import KafkaConfig
from applications.usecases.common.publisher import ApplicationPublish


@mock.patch("applications.infrastructure.broker.provider.KafkaBroker")
async def test_get_broker(fake_kafka_broker: mock.MagicMock) -> None:
    fake_config = mock.Mock()
    fake_config.uri = mock.Mock(return_value="fake url")

    async for _ in get_broker(fake_config):
        pass
    fake_kafka_broker.assert_called_once_with(fake_config.uri)


@pytest.fixture(scope="session")
async def broker() -> AsyncIterable[KafkaBroker]:
    broker = KafkaBroker(KafkaConfig("127.0.0.1", "9092").uri)
    async with TestKafkaBroker(broker) as br:
        yield br


async def test_publisher_kafka(broker: KafkaBroker) -> None:
    app_pub = ApplicationPublisherKafka(broker, AppTopic("Test"))
    new_application = ApplicationService.create_application(
        "Maclovi",
        "Some Description",
    )
    await app_pub.publish(ApplicationPublish.from_entity(new_application))
