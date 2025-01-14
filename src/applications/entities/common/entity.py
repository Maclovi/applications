from dataclasses import dataclass
from typing import Generic, TypeVar

OIDType = TypeVar("OIDType")


@dataclass
class Entity(Generic[OIDType]):
    oid: OIDType
