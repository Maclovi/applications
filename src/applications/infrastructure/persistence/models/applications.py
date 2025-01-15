import sqlalchemy as sa
from sqlalchemy.orm import composite

from applications.entities.application.models import Application
from applications.entities.application.value_objects import (
    ApplicationDescription,
)
from applications.entities.common.value_objects import Username
from applications.infrastructure.persistence.models.base import mapper_registry

applications_table = sa.Table(
    "applications",
    mapper_registry.metadata,
    sa.Column(
        "id",
        sa.BigInteger,
        primary_key=True,
        autoincrement=True,
    ),
    sa.Column("username", sa.String(32), nullable=False),
    sa.Column("application_description", sa.String(5000), nullable=False),
    sa.Column(
        "created_at",
        sa.DateTime,
        default=sa.func.now(),
        server_default=sa.func.now(),
        nullable=False,
    ),
    sa.Column(
        "updated_at",
        sa.DateTime,
        default=sa.func.now(),
        server_default=sa.func.now(),
        onupdate=sa.func.now(),
        server_onupdate=sa.func.now(),
        nullable=True,
    ),
)


def map_applications_table() -> None:
    _ = mapper_registry.map_imperatively(
        Application,
        applications_table,
        properties={
            "oid": applications_table.c.id,
            "user_name": composite(Username, applications_table.c.username),
            "description": composite(
                ApplicationDescription,
                applications_table.c.application_description,
            ),
        },
    )
