from dataclasses import dataclass

from applications.entities.application.errors import (
    ApplicationDescriptionLengthError,
)


@dataclass(slots=True, frozen=True, eq=True, unsafe_hash=True)
class ApplicationDescription:
    value: str

    def __post_init__(self) -> None:
        description_max_length = 1000
        if len(self.value) > description_max_length:
            raise ApplicationDescriptionLengthError(description_max_length)
