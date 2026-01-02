import pytest


@pytest.fixture
def mock_settings():
    """Mock settings for testing."""
    from unittest.mock import MagicMock

    settings = MagicMock()
    settings.FIGMA_ACCESS_TOKEN = "test_token"
    settings.FIGMA_API_BASE_URL = "https://api.figma.com/v1"
    settings.REQUEST_TIMEOUT = 60
    settings.headers = {"X-Figma-Token": "test_token"}
    return settings


@pytest.fixture
def mock_figma_service(mock_settings):
    """Mock Figma service for testing."""
    from unittest.mock import AsyncMock, MagicMock

    service = MagicMock()
    service.settings = mock_settings
    service.get_file = AsyncMock(return_value={"name": "Test File"})
    service.get_file_nodes = AsyncMock(return_value={"nodes": {}})
    service.get_images = AsyncMock(return_value={"images": {}})
    service.get_components = AsyncMock(return_value={"meta": {"components": []}})
    service.get_styles = AsyncMock(return_value={"meta": {"styles": []}})
    service.get_comments = AsyncMock(return_value={"comments": []})
    return service
