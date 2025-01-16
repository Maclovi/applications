from typing import NewType, final

from faststream.confluent import KafkaBroker
from typing_extensions import override

from applications.entities.application.models import Application
from applications.usecases.common.persistence.view_models import (
    ApplicationView,
)
from applications.usecases.common.publisher import ApplicationPublisher

AppTopic = NewType("AppTopic", str)


@final
class ApplicationPublisherKafka(ApplicationPublisher):
    def __init__(self, broker: KafkaBroker, topic: AppTopic) -> None:
        self._broker = broker
        self._app_topic = topic

    @override
    async def publish(self, application: Application) -> None:
        dto = ApplicationView(
            application.oid,
            application.user_name.value,
            application.description.value,
            application.created_at,
        )
        await self._broker.publish(
            dto,
            self._app_topic,
            headers={"content-type": "application/json"},
        )
