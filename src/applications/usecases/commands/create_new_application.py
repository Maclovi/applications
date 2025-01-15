from dataclasses import dataclass
from typing import final

from applications.entities.application.models import ApplicationID
from applications.entities.application.services import ApplicationService
from applications.usecases.common.publisher import ApplicationPublisher
from applications.usecases.common.transaction import EntitySaver, Transaction


@dataclass(frozen=True, slots=True)
class NewApplicationCommand:
    username: str
    description: str


@final
class NewApplicationCommandHandler:
    def __init__(
        self,
        application_service: ApplicationService,
        entity_saver: EntitySaver,
        transaction: Transaction,
        application_publisher: ApplicationPublisher,
    ) -> None:
        self._application_service = application_service
        self._entity_saver = entity_saver
        self._transaction = transaction
        self._application_publisher = application_publisher

    async def handle(self, data: NewApplicationCommand) -> ApplicationID:
        new_application = self._application_service.create_application(
            data.username,
            data.description,
        )
        self._entity_saver.add_one(new_application)
        await self._transaction.commit()
        await self._application_publisher.publish(new_application)
        return new_application.oid
