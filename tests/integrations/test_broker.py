from collections.abc import AsyncIterable

import pytest
from faststream.confluent import KafkaBroker, TestKafkaBroker

from applications.entities.application.services import ApplicationService
from applications.infrastructure.broker.config import KafkaConfig
from applications.infrastructure.broker.provider import get_broker
from applications.infrastructure.broker.publisher import (
    ApplicationPublisherKafka,
)


@pytest.fixture(scope="session")
async def broker() -> AsyncIterable[KafkaBroker]:
    broker = get_broker(KafkaConfig("127.0.0.1", "9092"))
    async with TestKafkaBroker(broker) as br:
        yield br


async def test_publisher_kafka(broker: KafkaBroker) -> None:
    publisher = ApplicationPublisherKafka(broker.publisher("Test"))
    new_application = ApplicationService.create_application(
        "Maclovi",
        "Some Description",
    )
    await publisher.publish(new_application)
