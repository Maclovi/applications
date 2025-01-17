from fastapi import Query
from pydantic import BaseModel

from applications.usecases.common.persistence.filters import SortOrder


class GetApplicationsSchema(BaseModel):
    user_name: str | None = None
    page: int = 1
    size: int = Query(10, le=1000)
    order: SortOrder = SortOrder.ASC
