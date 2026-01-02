import logging
from typing import Any, Optional

import httpx

from src.core.settings import Settings, get_settings


class FigmaService:
    """Сервис для работы с Figma API."""

    def __init__(self, settings: Optional[Settings] = None):
        self.settings = settings or get_settings()
        self.logger = logging.getLogger("mcp_figma.service")

    def _get_client(self) -> httpx.AsyncClient:
        """Создать HTTP клиент с настройками."""
        return httpx.AsyncClient(
            base_url=self.settings.FIGMA_API_BASE_URL,
            headers=self.settings.headers,
            timeout=self.settings.REQUEST_TIMEOUT,
        )

    async def get_file(
        self,
        file_key: str,
        version: Optional[str] = None,
        depth: Optional[int] = None,
    ) -> dict[str, Any]:
        """Получить данные файла Figma."""
        params: dict[str, Any] = {}
        if version:
            params["version"] = version
        if depth:
            params["depth"] = depth

        async with self._get_client() as client:
            response = await client.get(f"/files/{file_key}", params=params or None)
            response.raise_for_status()
            return response.json()

    async def get_file_nodes(
        self,
        file_key: str,
        node_ids: list[str],
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """Получить конкретные ноды из файла."""
        params: dict[str, Any] = {"ids": ",".join(node_ids)}
        if version:
            params["version"] = version

        async with self._get_client() as client:
            response = await client.get(f"/files/{file_key}/nodes", params=params)
            response.raise_for_status()
            return response.json()

    async def get_images(
        self,
        file_key: str,
        node_ids: list[str],
        scale: Optional[float] = None,
        format: Optional[str] = None,
        version: Optional[str] = None,
    ) -> dict[str, Any]:
        """Экспортировать изображения нод."""
        params: dict[str, Any] = {"ids": ",".join(node_ids)}
        if scale:
            params["scale"] = scale
        if format:
            params["format"] = format
        if version:
            params["version"] = version

        async with self._get_client() as client:
            response = await client.get(f"/images/{file_key}", params=params)
            response.raise_for_status()
            return response.json()

    async def get_components(self, file_key: str) -> dict[str, Any]:
        """Получить все компоненты файла."""
        async with self._get_client() as client:
            response = await client.get(f"/files/{file_key}/components")
            response.raise_for_status()
            return response.json()

    async def get_styles(self, file_key: str) -> dict[str, Any]:
        """Получить все стили файла."""
        async with self._get_client() as client:
            response = await client.get(f"/files/{file_key}/styles")
            response.raise_for_status()
            return response.json()

    async def get_comments(self, file_key: str) -> dict[str, Any]:
        """Получить комментарии к файлу."""
        async with self._get_client() as client:
            response = await client.get(f"/files/{file_key}/comments")
            response.raise_for_status()
            return response.json()

    async def get_team_projects(self, team_id: str) -> dict[str, Any]:
        """Получить проекты команды."""
        async with self._get_client() as client:
            response = await client.get(f"/teams/{team_id}/projects")
            response.raise_for_status()
            return response.json()

    async def get_project_files(self, project_id: str) -> dict[str, Any]:
        """Получить файлы проекта."""
        async with self._get_client() as client:
            response = await client.get(f"/projects/{project_id}/files")
            response.raise_for_status()
            return response.json()
