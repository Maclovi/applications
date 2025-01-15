from dataclasses import dataclass
from typing import final

from applications.usecases.common.ports.application import (
    ApplicationReader,
    ApplicationReaderFilters,
)
from applications.usecases.common.ports.filters import Pagination
from applications.usecases.common.ports.view_models import ApplicationView


@dataclass(frozen=True, slots=True)
class GetApplicationsQuery:
    filters: ApplicationReaderFilters
    pagination: Pagination


@final
class GetApplicationsQueryHandler:
    def __init__(self, application_reader: ApplicationReader) -> None:
        self._application_reader = application_reader

    async def handle(
        self,
        data: GetApplicationsQuery,
    ) -> list[ApplicationView]:
        return await self._application_reader.read_many(
            data.filters,
            data.pagination,
        )
