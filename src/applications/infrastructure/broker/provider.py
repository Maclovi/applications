from faststream.confluent import KafkaBroker

from applications.infrastructure.broker.config import KafkaConfig


def get_broker(config: KafkaConfig) -> KafkaBroker:
    return KafkaBroker(f"{config.host}:{config.port}")
