from applications.entities.application.services import ApplicationService
from applications.entities.application.value_objects import (
    ApplicationDescription,
)
from applications.entities.common.value_objects import Username


def test_create_application() -> None:
    application = ApplicationService.create_application(
        Username("Maclovi"),
        ApplicationDescription("Some description"),
    )
    assert isinstance(application.user_name, Username)
    assert isinstance(application.description, ApplicationDescription)
    assert application.oid is None
