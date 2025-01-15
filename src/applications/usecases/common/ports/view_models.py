from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class ApplicationView:
    id: int
    user_name: str
    description: str
    created_at: datetime
