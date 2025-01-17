from unittest import mock

from applications.usecases.commands.create_new_application import (
    NewApplicationCommand,
    NewApplicationCommandHandler,
)
from applications.usecases.common.publisher import ApplicationPublish


async def test_new_application_handler(
    fake_application_service: mock.Mock,
    fake_entity_saver: mock.Mock,
    fake_transaction: mock.Mock,
    fake_application_publisher: mock.Mock,
) -> None:
    dto = NewApplicationCommand(
        user_name="Maclovi",
        description="Some description",
    )
    interactor = NewApplicationCommandHandler(
        fake_application_service,
        fake_entity_saver,
        fake_transaction,
        fake_application_publisher,
    )
    oid = await interactor.handle(dto)

    fake_application_service.create_application.assert_called_once_with(
        dto.user_name,
        dto.description,
    )
    new_application = fake_application_service.create_application(
        dto.user_name,
        dto.description,
    )
    fake_entity_saver.add_one.assert_called_once_with(new_application)
    fake_transaction.commit.assert_called_once()
    fake_application_publisher.publish.assert_called_once_with(
        ApplicationPublish.from_entity(new_application),
    )
    assert oid is None
