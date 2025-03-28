from typing import TYPE_CHECKING

from starlette.middleware.cors import CORSMiddleware

from applications.presentation.http.middlewares.metrics import (
    MetricsMiddleware,
)

if TYPE_CHECKING:
    from fastapi import FastAPI

    from applications.infrastructure.configs import APIConfig


def setup_middlewares(app: "FastAPI", /, api_config: "APIConfig") -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            f"http://localhost:{api_config.port}",
            f"http://{api_config.host}:{api_config.port}",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(MetricsMiddleware)
