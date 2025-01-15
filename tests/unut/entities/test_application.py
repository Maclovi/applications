from datetime import datetime
from typing import cast

from applications.entities.application.services import ApplicationService
from applications.entities.application.value_objects import (
    ApplicationDescription,
)
from applications.entities.common.value_objects import Username


def test_create_application() -> None:
    application = ApplicationService.create_application(
        "Maclovi",
        "Some description",
    )
    assert isinstance(application.user_name, Username)
    assert isinstance(application.description, ApplicationDescription)
    assert application.oid is cast(int, cast(object, None))
    assert application.created_at is cast(datetime, cast(object, None))
