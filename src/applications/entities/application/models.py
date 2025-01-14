from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from applications.entities.application.value_objects import (
    ApplicationDescription,
)
from applications.entities.common.entity import Entity

ApplicationID = NewType("ApplicationID", int)


@dataclass
class Application(Entity[ApplicationID]):
    user_name: str
    description: ApplicationDescription
    create_at: datetime
