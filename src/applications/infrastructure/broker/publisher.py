from typing import final

from faststream.confluent import KafkaBroker
from typing_extensions import override

from applications.entities.application.models import Application
from applications.usecases.common.publisher import ApplicationPublisher


@final
class ApplicationPublisherKafka(ApplicationPublisher):
    def __init__(self, broker: KafkaBroker) -> None:
        self._broker = broker

    @override
    async def publish(self, application: Application) -> None:
        raise NotImplementedError
