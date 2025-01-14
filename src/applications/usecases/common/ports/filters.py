from dataclasses import dataclass
from enum import Enum


class SortOrder(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclass(frozen=True)
class Pagination:
    page: int | None = None
    size: int | None = None
    order: SortOrder = SortOrder.ASC
