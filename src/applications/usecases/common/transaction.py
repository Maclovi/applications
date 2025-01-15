from abc import abstractmethod
from typing import Protocol

from applications.entities.common.entity import Entity, OIDType


class Transaction(Protocol):
    @abstractmethod
    async def commit(self) -> None: ...


class EntitySaver:
    @abstractmethod
    def add_one(self, entity: Entity[OIDType]) -> None: ...
