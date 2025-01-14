from abc import abstractmethod
from typing import Protocol

from applications.entities.common.entity import Entity, OIDType


class Transaction(Protocol):
    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def flush(self) -> None: ...


class EntitySaver:
    @abstractmethod
    def add_one(self, entity: Entity[OIDType]) -> None: ...

    @abstractmethod
    async def delete(self, entity: Entity[OIDType]) -> None: ...
