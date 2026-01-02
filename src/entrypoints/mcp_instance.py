from fastmcp import FastMCP

from src.core.settings import get_settings

settings = get_settings()

mcp = FastMCP(
    name=settings.APP_NAME,
    instructions="""
    Figma MCP Server - сервер для работы с Figma API.

    Возможности:
    - Получение данных файлов и нод
    - Экспорт изображений компонентов
    - Получение компонентов и стилей
    - Работа с командами и проектами
    - Получение комментариев

    Для работы требуется персональный токен доступа Figma (FIGMA_ACCESS_TOKEN).
    """,
)
