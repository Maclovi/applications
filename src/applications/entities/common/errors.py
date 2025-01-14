from typing_extensions import override


class DomainError(Exception):
    @property
    def message(self) -> str:
        raise NotImplementedError


class FieldError(DomainError):
    pass


class InvalidUsernameError(FieldError):
    @property
    @override
    def message(self) -> str:
        return (
            "You can use A-Z, a-z, 0-9 and underscores. "
            "Minimum length is 5 characters, maximum is 32. "
            "Like telegram username regex. "
            "Example: My_user_name123."
        )
