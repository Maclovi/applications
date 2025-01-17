from dishka import Provider, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from applications.entities.application.services import ApplicationService
from applications.infrastructure.broker.provider import (
    get_broker,
)
from applications.infrastructure.broker.publisher import (
    ApplicationPublisherKafka,
    AppTopic,
)
from applications.infrastructure.configs import (
    APIConfig,
    KafkaConfig,
    PostgresConfig,
)
from applications.infrastructure.persistence.actions.application import (
    ApplicationReaderAlchemy,
)
from applications.infrastructure.persistence.provider import (
    get_engine,
    get_session,
    get_sessionmaker,
)
from applications.infrastructure.persistence.transaction import (
    EntitySaverAlchemy,
    TransactionAlchemy,
)
from applications.usecases.commands.create_new_application import (
    NewApplicationCommandHandler,
)
from applications.usecases.common.persistence.application import (
    ApplicationReader,
)
from applications.usecases.common.persistence.transaction import (
    EntitySaver,
    Transaction,
)
from applications.usecases.common.publisher import ApplicationPublisher
from applications.usecases.queries.get_all_applications import (
    GetApplicationsQueryHandler,
)


def configs_provider() -> Provider:
    provider = Provider()
    provider.from_context(provides=APIConfig, scope=Scope.APP)
    provider.from_context(provides=PostgresConfig, scope=Scope.APP)
    provider.from_context(provides=KafkaConfig, scope=Scope.APP)
    return provider


def db_provider() -> Provider:
    provider = Provider()
    provider.provide(get_engine, scope=Scope.APP)
    provider.provide(get_sessionmaker, scope=Scope.APP)
    provider.provide(get_session, provides=AsyncSession, scope=Scope.REQUEST)
    return provider


def broker_provider() -> Provider:
    provider = Provider(scope=Scope.APP)
    provider.provide(get_broker)
    provider.provide(lambda: AppTopic("Kafka"), provides=AppTopic)
    provider.provide(ApplicationPublisherKafka, provides=ApplicationPublisher)
    return provider


def persistence_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    provider.provide(TransactionAlchemy, provides=Transaction)
    provider.provide(EntitySaverAlchemy, provides=EntitySaver)
    provider.provide(ApplicationReaderAlchemy, provides=ApplicationReader)
    return provider


def interactors_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    provider.provide_all(
        NewApplicationCommandHandler,
        GetApplicationsQueryHandler,
    )
    return provider


def services_provider() -> Provider:
    provider = Provider()
    provider.provide(ApplicationService, scope=Scope.APP)
    return provider


def setup_providers() -> tuple[Provider, ...]:
    return (
        configs_provider(),
        db_provider(),
        persistence_provider(),
        broker_provider(),
        interactors_provider(),
        services_provider(),
    )
