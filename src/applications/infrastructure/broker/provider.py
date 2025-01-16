from collections.abc import AsyncIterable

from faststream.confluent import KafkaBroker

from applications.infrastructure.configs import KafkaConfig


async def get_broker(config: KafkaConfig) -> AsyncIterable[KafkaBroker]:
    async with KafkaBroker(config.uri) as broker:
        yield broker
