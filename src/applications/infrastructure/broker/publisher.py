from typing import NewType, final

from faststream.confluent import KafkaBroker
from typing_extensions import override

from applications.usecases.common.publisher import (
    ApplicationPublish,
    ApplicationPublisher,
)

AppTopic = NewType("AppTopic", str)


@final
class ApplicationPublisherKafka(ApplicationPublisher):
    def __init__(self, broker: KafkaBroker, topic: AppTopic) -> None:
        self._broker = broker
        self._app_topic = topic

    @override
    async def publish(self, application: ApplicationPublish) -> None:
        await self._broker.publish(
            application,
            self._app_topic,
            headers={"content-type": "application/json"},
        )
