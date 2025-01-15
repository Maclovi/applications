from datetime import datetime
from typing import cast

from applications.entities.application.models import Application, ApplicationID
from applications.entities.application.value_objects import (
    ApplicationDescription,
)
from applications.entities.common.value_objects import Username


class ApplicationService:
    @staticmethod
    def create_application(
        user_name: str,
        description: str,
    ) -> Application:
        return Application(
            oid=cast(ApplicationID, cast(object, None)),
            user_name=Username(user_name),
            description=ApplicationDescription(description),
            created_at=cast(datetime, cast(object, None)),
        )
