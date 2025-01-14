import re
from dataclasses import dataclass

from applications.entities.common.errors import InvalidUsernameError

validate_username = re.compile(r"[A-Za-z][A-Za-z0-9_]{4,31}").fullmatch


@dataclass(slots=True, frozen=True, eq=True, unsafe_hash=True)
class Username:
    value: str

    def __post_init__(self) -> None:
        """
        You can use A-Z, a-z, 0-9 and underscores.
        Minimum length is 5 characters, maximum is 32.
        Like telegram username regex.
        Example: My_user_name123.
        """
        if (
            not validate_username(self.value)
            or self.value.endswith("_")
            or "__" in self.value
        ):
            raise InvalidUsernameError
