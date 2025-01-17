from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Query, status

from applications.entities.application.models import ApplicationID
from applications.presentation.http.routes.schemes import GetApplicationsSchema
from applications.usecases.commands.create_new_application import (
    NewApplicationCommand,
    NewApplicationCommandHandler,
)
from applications.usecases.common.persistence.application import (
    ApplicationReaderFilters,
)
from applications.usecases.common.persistence.filters import Pagination
from applications.usecases.queries.get_all_applications import (
    ApplicationsResponse,
    GetApplicationsQuery,
    GetApplicationsQueryHandler,
)

route = APIRouter(
    prefix="/applications",
    tags=["Applications"],
    route_class=DishkaRoute,
)


@route.post(
    "",
    summary="Create one application",
    status_code=status.HTTP_200_OK,
)
async def new_application(
    dto: NewApplicationCommand,
    interactor: FromDishka[NewApplicationCommandHandler],
) -> ApplicationID:
    return await interactor.handle(dto)


@route.get("")
async def get_applications(
    schema: Annotated[GetApplicationsSchema, Query()],
    interactor: FromDishka[GetApplicationsQueryHandler],
) -> ApplicationsResponse:
    dto = GetApplicationsQuery(
        filters=ApplicationReaderFilters(user_name=schema.user_name),
        pagination=Pagination(
            page=schema.page,
            size=schema.size,
            order=schema.order,
        ),
    )
    return await interactor.handle(dto)
