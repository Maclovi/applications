from applications.entities.common.value_objects import Username
from applications.usecases.common.errors import MaxSizePaginationError


def validate_username(username: str | None) -> None:
    Username(username) if username else None


def validate_max_size_pagination(size: int) -> None:
    max_size_pagination = 1000
    if size > max_size_pagination:
        raise MaxSizePaginationError(max_size_pagination)
