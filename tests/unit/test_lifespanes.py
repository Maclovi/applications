from unittest import mock

from applications.infrastructure.persistence.provider import get_engine
from applications.web import lifespan


@mock.patch(
    "applications.infrastructure.persistence.provider.create_async_engine",
)
async def test_engine(fake_create_async_engine: mock.MagicMock) -> None:
    fake_create_async_engine.return_value.dispose = mock.AsyncMock()
    fake_config = mock.Mock()
    async for _ in get_engine(fake_config):
        pass
    fake_create_async_engine.return_value.dispose.assert_called_once()


async def test_lifespan() -> None:
    fake_app = mock.Mock()
    fake_app.state.dishka_container.close = mock.AsyncMock()
    async with lifespan(fake_app):
        pass
    fake_app.state.dishka_container.close.assert_called_once()
