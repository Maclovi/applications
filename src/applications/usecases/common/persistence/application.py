from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

from applications.usecases.common.persistence.filters import Pagination
from applications.usecases.common.persistence.view_models import (
    ApplicationView,
)


@dataclass(frozen=True, slots=True)
class ApplicationReaderFilters:
    user_name: str | None = None


class ApplicationReader(Protocol):
    @abstractmethod
    async def read_many(
        self,
        filters: ApplicationReaderFilters,
        pagination: Pagination,
    ) -> list[ApplicationView]: ...
