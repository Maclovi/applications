from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

from applications.entities.common.value_objects import Username
from applications.usecases.common.ports.filters import Pagination


@dataclass(frozen=True, slots=True)
class ApplicationsReaderFilters:
    user_name: Username | None = None


class ApplicationsReader(Protocol):
    @abstractmethod
    async def read_many(
        self,
        filters: ApplicationsReaderFilters,
        pagination: Pagination,
    ) -> None: ...
