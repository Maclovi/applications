from datetime import datetime, timezone
from unittest import mock

import pytest

from applications.entities.common.errors import (
    InvalidUsernameError,
)
from applications.usecases.common.errors import (
    MaxSizePaginationError,
    SatisfiedError,
)
from applications.usecases.common.persistence.application import (
    ApplicationReaderFilters,
)
from applications.usecases.common.persistence.filters import Pagination
from applications.usecases.queries.get_all_applications import (
    GetApplicationsQuery,
    GetApplicationsQueryHandler,
)


@pytest.mark.parametrize(
    ("username", "pagination_size", "exc_class"),
    [
        ("_Maclovi", 10, InvalidUsernameError),
        ("Maclovi", 1001, MaxSizePaginationError),
        ("Maclovi", 1000, None),
    ],
)
async def test_get_application_query_handler(
    username: str | None,
    pagination_size: int,
    exc_class: type[SatisfiedError] | None,
    fake_application_reader: mock.Mock,
) -> None:
    dto = GetApplicationsQuery(
        filters=ApplicationReaderFilters(user_name=username),
        pagination=Pagination(size=pagination_size),
    )
    interactor = GetApplicationsQueryHandler(fake_application_reader)
    if exc_class:
        with pytest.raises(exc_class) as excinfo:
            await interactor.handle(dto)

        if exc_class is MaxSizePaginationError:
            assert excinfo.value.message == "Max size pagination is 1000"
    else:
        results = await interactor.handle(dto)
        fake_application_reader.read_many.assert_called_once_with(
            dto.filters,
            dto.pagination,
        )
        application_view = results[0]
        assert application_view.id == 1
        assert application_view.user_name == "Maclovi"
        assert application_view.description == "Some Description"
        new_date = datetime.now(timezone.utc).replace(microsecond=0)
        assert application_view.created_at.replace(microsecond=0) == new_date
