from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Query

from applications.entities.application.models import ApplicationID
from applications.entities.common.value_objects import Username
from applications.presentation.http.routes.schemes import GetApplicationsSchema
from applications.usecases.commands.create_new_application import (
    NewApplicationCommand,
    NewApplicationCommandHandler,
)
from applications.usecases.common.persistence.application import (
    ApplicationReaderFilters,
)
from applications.usecases.common.persistence.filters import Pagination
from applications.usecases.common.persistence.view_models import (
    ApplicationView,
)
from applications.usecases.queries.get_all_applications import (
    GetApplicationsQuery,
    GetApplicationsQueryHandler,
)

route = APIRouter(
    prefix="/application",
    tags=["Applications"],
    route_class=DishkaRoute,
)


@route.post("")
async def new_application(
    dto: NewApplicationCommand,
    interactor: FromDishka[NewApplicationCommandHandler],
) -> ApplicationID:
    return await interactor.handle(dto)


@route.get("")
async def get_applications(
    schema: Annotated[GetApplicationsSchema, Query()],
    interactor: FromDishka[GetApplicationsQueryHandler],
) -> list[ApplicationView]:
    dto = GetApplicationsQuery(
        filters=ApplicationReaderFilters(
            user_name=Username(schema.user_name) if schema.user_name else None,
        ),
        pagination=Pagination(
            page=schema.page,
            size=schema.size,
            order=schema.order,
        ),
    )
    return await interactor.handle(dto)
