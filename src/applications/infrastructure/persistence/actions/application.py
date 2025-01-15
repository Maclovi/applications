from typing import final

from sqlalchemy import RowMapping, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import override

from applications.infrastructure.persistence.models.applications import (
    applications_table,
)
from applications.usecases.common.persistence.application import (
    ApplicationReader,
    ApplicationReaderFilters,
)
from applications.usecases.common.persistence.filters import Pagination
from applications.usecases.common.persistence.view_models import (
    ApplicationView,
)


@final
class ApplicationReaderAlchemy(ApplicationReader):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    def _load_applicationsview(self, row: RowMapping) -> ApplicationView:
        return ApplicationView(
            row.id,
            row.username,
            row.application_description,
            row.created_at,
        )

    @override
    async def read_many(
        self,
        filters: ApplicationReaderFilters,
        pagination: Pagination,
    ) -> list[ApplicationView]:
        offset = (pagination.page - 1) * pagination.size
        stmt = (
            select(
                applications_table.c.id,
                applications_table.c.username,
                applications_table.c.application_description,
                applications_table.c.created_at,
            )
            .offset(offset)
            .limit(pagination.size)
        )
        if filters.user_name:
            stmt = stmt.where(
                applications_table.c.username == filters.user_name,
            )
        results = await self._session.execute(stmt)
        return [self._load_applicationsview(row) for row in results.mappings()]
