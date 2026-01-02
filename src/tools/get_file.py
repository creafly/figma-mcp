from typing import Optional

from src.core.validators import validate_file_key, validate_version
from src.entrypoints.mcp_instance import mcp
from src.services.figma_service import FigmaService


@mcp.tool()
async def get_file(
    file_key: str,
    version: Optional[str] = None,
    depth: Optional[int] = None,
) -> dict:
    """
    Получить данные файла Figma.

    Args:
        file_key: Ключ файла Figma (из URL)
        version: Версия файла (опционально)
        depth: Глубина вложенности нод (опционально)

    Returns:
        Данные файла включая структуру нод, стили и компоненты
    """
    file_key = validate_file_key(file_key)
    version = validate_version(version)

    service = FigmaService()
    return await service.get_file(file_key, version=version, depth=depth)
