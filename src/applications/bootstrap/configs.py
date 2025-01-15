from dataclasses import dataclass
from os import environ as env

from applications.infrastructure.broker.config import KafkaConfig
from applications.infrastructure.persistence.config import PostgresConfig


@dataclass(frozen=True, slots=True)
class APIConfig:
    host: str
    port: str


@dataclass(frozen=True, slots=True)
class Configs:
    kafka: KafkaConfig
    postgres: PostgresConfig
    web: APIConfig


def load_configs() -> Configs:
    return Configs(
        kafka=KafkaConfig(
            host=env["KAFKA_HOST"],
            port=env["KAFKA_PORT"],
        ),
        postgres=PostgresConfig(
            user=env["POSTGRES_USER"],
            password=env["POSTGRES_PASSWORD"],
            host=env["POSTGRES_HOST"],
            port=env["POSTGRES_PORT"],
            db_name=env["POSTGRES_DB"],
            debug=env["POSTGRES_DEBUG"] == "true",
        ),
        web=APIConfig(
            host=env["UVICORN_HOST"],
            port=env["UVICORN_PORT"],
        ),
    )
