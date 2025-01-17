from datetime import datetime, timezone
from unittest import mock

import pytest

from applications.usecases.common.persistence.application import (
    ApplicationReader,
)
from applications.usecases.common.persistence.view_models import (
    ApplicationView,
)


@pytest.fixture
def fake_application_reader() -> ApplicationReader:
    application_view = ApplicationView(
        1,
        "Maclovi",
        "Some Description",
        datetime.now(tz=timezone.utc),
    )
    fake = mock.Mock()
    fake.read_many = mock.AsyncMock(return_value=[application_view])
    return fake
