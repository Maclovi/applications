from dataclasses import dataclass

from typing_extensions import override

from applications.entities.common.errors import FieldError


@dataclass(eq=False)
class ApplicationDescriptionLengthError(FieldError):
    length: int

    @property
    @override
    def message(self) -> str:
        return f"The description length should not exceed {self.length!r}"
