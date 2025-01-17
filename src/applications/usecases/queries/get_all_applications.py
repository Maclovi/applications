from dataclasses import dataclass
from typing import final

from applications.usecases.common.persistence.application import (
    ApplicationReader,
    ApplicationReaderFilters,
)
from applications.usecases.common.persistence.filters import (
    Pagination,
    set_offset,
)
from applications.usecases.common.persistence.view_models import (
    ApplicationView,
)
from applications.usecases.common.validations import (
    validate_max_size_pagination,
    validate_username,
)


@dataclass(frozen=True, slots=True)
class GetApplicationsQuery:
    filters: ApplicationReaderFilters
    pagination: Pagination


@dataclass(frozen=True, slots=True)
class ApplicationsResponse:
    total: int
    applications: list[ApplicationView]


@final
class GetApplicationsQueryHandler:
    def __init__(self, application_reader: ApplicationReader) -> None:
        self._application_reader = application_reader

    async def handle(
        self,
        data: GetApplicationsQuery,
    ) -> ApplicationsResponse:
        validate_username(data.filters.user_name)
        validate_max_size_pagination(data.pagination.size)
        data.pagination.page = set_offset(data.pagination)
        results = await self._application_reader.read_many(
            data.filters,
            data.pagination,
        )
        return ApplicationsResponse(total=len(results), applications=results)
