from dataclasses import dataclass
from enum import Enum


class SortOrder(str, Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclass(slots=True)
class Pagination:
    page: int = 1
    size: int = 10
    order: SortOrder = SortOrder.ASC


def set_offset(pagination: Pagination) -> int:
    return (pagination.page - 1) * pagination.size
