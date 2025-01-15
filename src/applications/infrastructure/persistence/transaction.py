from typing import Final

from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import override

from applications.entities.common.entity import Entity, OIDType
from applications.usecases.common.persistence.transaction import (
    EntitySaver,
    Transaction,
)


class TransactionAlchemy(Transaction):
    def __init__(self, session: AsyncSession) -> None:
        self._session: Final[AsyncSession] = session

    @override
    async def commit(self) -> None:
        await self._session.commit()


class EntitySaverAlchemy(EntitySaver):
    def __init__(self, session: AsyncSession) -> None:
        self._session: Final[AsyncSession] = session

    @override
    def add_one(self, entity: Entity[OIDType]) -> None:
        self._session.add(entity)
