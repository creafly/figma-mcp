from src.entrypoints.mcp_instance import mcp
from src.services.figma_service import FigmaService


@mcp.tool()
async def get_team_projects(team_id: str) -> dict:
    """
    Получить проекты команды.

    Args:
        team_id: ID команды Figma

    Returns:
        Список проектов команды
    """
    if not team_id or not team_id.strip():
        raise ValueError("Team ID is required")

    service = FigmaService()
    return await service.get_team_projects(team_id.strip())


@mcp.tool()
async def get_project_files(project_id: str) -> dict:
    """
    Получить файлы проекта.

    Args:
        project_id: ID проекта Figma

    Returns:
        Список файлов в проекте
    """
    if not project_id or not project_id.strip():
        raise ValueError("Project ID is required")

    service = FigmaService()
    return await service.get_project_files(project_id.strip())
