from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from applications.entities.application.value_objects import (
    ApplicationDescription,
)
from applications.entities.common.entity import Entity
from applications.entities.common.value_objects import Username

ApplicationID = NewType("ApplicationID", int)


@dataclass
class Application(Entity[ApplicationID]):
    user_name: Username
    description: ApplicationDescription
    created_at: datetime
