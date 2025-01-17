from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PostgresConfig:
    user: str
    password: str
    host: str
    port: str
    db_name: str
    debug: bool

    @property
    def uri(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


@dataclass(frozen=True, slots=True)
class APIConfig:
    host: str
    port: str


@dataclass(frozen=True, slots=True)
class KafkaConfig:
    host: str
    port: str

    @property
    def uri(self) -> str:
        return f"{self.host}:{self.port}"
