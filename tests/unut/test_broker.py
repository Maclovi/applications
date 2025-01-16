from collections.abc import AsyncIterable

import pytest
from faststream.confluent import KafkaBroker, TestKafkaBroker

from applications.entities.application.services import ApplicationService
from applications.infrastructure.broker.publisher import (
    ApplicationPublisherKafka,
    AppTopic,
)
from applications.infrastructure.configs import KafkaConfig


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
    await app_pub.publish(new_application)
