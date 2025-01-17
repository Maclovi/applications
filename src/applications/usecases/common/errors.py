from dataclasses import dataclass

from typing_extensions import override


class ApplicationError(Exception):
    @property
    def message(self) -> str:
        raise NotImplementedError


class SatisfiedError(ApplicationError):
    pass


@dataclass(eq=False)
class MaxSizePaginationError(SatisfiedError):
    size: int

    @property
    @override
    def message(self) -> str:
        return f"Max size pagination is {self.size}"
