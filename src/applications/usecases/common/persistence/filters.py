from dataclasses import dataclass
from enum import Enum


class SortOrder(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclass(frozen=True)
class Pagination:
    page: int = 1
    size: int = 10
    order: SortOrder = SortOrder.ASC
