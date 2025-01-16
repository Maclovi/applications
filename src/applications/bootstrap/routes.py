from typing import TYPE_CHECKING

from applications.presentation.http.routes import application

if TYPE_CHECKING:
    from fastapi import FastAPI


def setup_routes(app: "FastAPI", /) -> None:
    app.include_router(application.route)
