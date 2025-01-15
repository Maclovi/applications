from unittest import mock

import pytest

from applications.entities.application.services import ApplicationService


@pytest.fixture
def fake_application_service() -> ApplicationService:
    fake = mock.Mock()
    fake.create_application = mock.Mock(
        side_effect=ApplicationService.create_application,
    )
    return fake


@pytest.fixture
def fake_entity_saver() -> ApplicationService:
    fake = mock.Mock()
    fake.add_one = mock.Mock()
    return fake


@pytest.fixture
def fake_transaction() -> ApplicationService:
    fake = mock.Mock()
    fake.commit = mock.AsyncMock()
    return fake


@pytest.fixture
def fake_application_publisher() -> ApplicationService:
    fake = mock.Mock()
    fake.publish = mock.AsyncMock()
    return fake
