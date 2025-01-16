from pydantic import BaseModel

from applications.usecases.common.persistence.filters import SortOrder


class GetApplicationsSchema(BaseModel):
    user_name: str | None = None
    page: int = 1
    size: int = 10
    order: SortOrder = SortOrder.ASC
