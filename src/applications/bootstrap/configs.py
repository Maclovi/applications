from os import environ as env
from typing import NamedTuple

from applications.infrastructure.configs import (
    APIConfig,
    KafkaConfig,
    PostgresConfig,
)


class ConfigsComposite(NamedTuple):
    kafka: KafkaConfig
    postgres: PostgresConfig
    web: APIConfig


def load_configs() -> ConfigsComposite:
    return ConfigsComposite(
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
