import pytest
from unittest.mock import patch


@pytest.fixture
def settings():
    return {
        "theme": "dark",
        "language": "English"
    }


def test_theme(settings):
    with patch.dict(settings, {"theme": "light"}):
        assert settings["theme"] == "light"


