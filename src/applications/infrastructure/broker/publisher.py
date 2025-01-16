from typing import final

from faststream.confluent.publisher.asyncapi import AsyncAPIDefaultPublisher
from typing_extensions import override

from applications.entities.application.models import Application
from applications.usecases.common.publisher import ApplicationPublisher


@final
class ApplicationPublisherKafka(ApplicationPublisher):
    def __init__(self, publisher: AsyncAPIDefaultPublisher) -> None:
        self._publisher = publisher

    @override
    async def publish(self, application: Application) -> None:
        _ = await self._publisher.publish(application)
