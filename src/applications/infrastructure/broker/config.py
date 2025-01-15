from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KafkaConfig:
    host: str
    port: str
