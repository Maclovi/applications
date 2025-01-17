import pytest

from applications.entities.application.errors import (
    ApplicationDescriptionLengthError,
)
from applications.entities.application.value_objects import (
    ApplicationDescription,
)
from applications.entities.common.errors import (
    FieldError,
    InvalidUsernameError,
)
from applications.entities.common.value_objects import Username

value_objects = pytest.mark.value_objects


@pytest.mark.parametrize(
    ("value", "exc_class"),
    [
        ("a", InvalidUsernameError),
        ("aaaa", InvalidUsernameError),
        ("a" * 33, InvalidUsernameError),
        ("_aaaaa", InvalidUsernameError),
        ("aaaaa_", InvalidUsernameError),
        ("aaa__aa", InvalidUsernameError),
        ("aaa_____aa", InvalidUsernameError),
        ("aaa___aa", InvalidUsernameError),
        ("9aaaaa", InvalidUsernameError),
        ("aaaaa", None),
        ("a" * 32, None),
        ("aaa_a_a", None),
        ("SomeUsername", None),
        ("Some_Username", None),
        ("Maclovi", None),
        ("Maclovi_Maclovi", None),
        ("maclovi_maclovi_12345", None),
    ],
)
def test_username(value: str, exc_class: type[FieldError] | None) -> None:
    if exc_class:
        with pytest.raises(exc_class) as excinfo:
            _ = Username(value)
        assert excinfo.value.message == (
            "You can use A-Z, a-z, 0-9 and underscores. "
            "Minimum length is 5 characters, maximum is 32. "
            "Like telegram username regex. "
            "Example: My_user_name123."
        )
    else:
        user_name = Username(value)
        assert isinstance(user_name, Username)
        assert user_name.value == value


@pytest.mark.parametrize(
    ("value", "exc_class"),
    [
        ("a" * 5001, ApplicationDescriptionLengthError),
        ("a" * 5000, None),
    ],
)
def test_application_description(
    value: str,
    exc_class: type[FieldError] | None,
) -> None:
    if exc_class:
        with pytest.raises(exc_class) as excinfo:
            ApplicationDescription(value)
        max_length = 5000
        msg = f"The description length should not exceed {max_length!r}"
        assert excinfo.value.message == msg
    else:
        application_description = ApplicationDescription(value)
        assert isinstance(application_description, ApplicationDescription)
        assert application_description.value == value
