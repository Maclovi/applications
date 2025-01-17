from functools import partial

from fastapi import FastAPI
from starlette import status as code

from applications.entities.common.errors import FieldError
from applications.presentation.http.exc_handlers import validate
from applications.usecases.common.errors import SatisfiedError


def setup_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        FieldError,
        partial(validate, status=code.HTTP_422_UNPROCESSABLE_ENTITY),
    )
    app.add_exception_handler(
        SatisfiedError,
        partial(validate, status=code.HTTP_400_BAD_REQUEST),
    )
