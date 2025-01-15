from datetime import datetime, timezone
from unittest import mock

from applications.usecases.common.ports.application import (
    ApplicationReaderFilters,
)
from applications.usecases.common.ports.filters import Pagination
from applications.usecases.queries.get_all_applications import (
    GetApplicationsQuery,
    GetApplicationsQueryHandler,
)


async def test_get_application_query_handler(
    fake_application_reader: mock.Mock,
) -> None:
    dto = GetApplicationsQuery(
        filters=ApplicationReaderFilters(),
        pagination=Pagination(),
    )
    interactor = GetApplicationsQueryHandler(fake_application_reader)
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
