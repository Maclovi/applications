from abc import abstractmethod

from applications.entities.application.models import Application


class ApplicationPublisher:
    @abstractmethod
    async def publish(self, application: Application) -> None: ...
