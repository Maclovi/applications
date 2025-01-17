from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime

from typing_extensions import Self

from applications.entities.application.models import Application


@dataclass(frozen=True, slots=True)
class ApplicationPublish:
    id: int
    username: str
    description: str
    created_at: datetime

    @classmethod
    def from_entity(cls, application: Application) -> Self:
        return cls(
            application.oid,
            application.user_name.value,
            application.description.value,
            application.created_at,
        )


class ApplicationPublisher:
    @abstractmethod
    async def publish(self, application: ApplicationPublish) -> None: ...
