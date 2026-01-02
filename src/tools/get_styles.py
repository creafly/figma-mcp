from src.core.validators import validate_file_key
from src.entrypoints.mcp_instance import mcp
from src.services.figma_service import FigmaService


@mcp.tool()
async def get_styles(file_key: str) -> dict:
    """
    Получить все стили из файла Figma.

    Args:
        file_key: Ключ файла Figma (из URL)

    Returns:
        Список стилей (цвета, эффекты, текстовые стили и т.д.)
    """
    file_key = validate_file_key(file_key)

    service = FigmaService()
    return await service.get_styles(file_key)
