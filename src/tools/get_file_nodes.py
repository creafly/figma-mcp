from typing import Optional

from src.core.validators import validate_file_key, validate_node_ids, validate_version
from src.entrypoints.mcp_instance import mcp
from src.services.figma_service import FigmaService


@mcp.tool()
async def get_file_nodes(
    file_key: str,
    node_ids: list[str],
    version: Optional[str] = None,
) -> dict:
    """
    Получить конкретные ноды из файла Figma.

    Args:
        file_key: Ключ файла Figma (из URL)
        node_ids: Список ID нод (формат: "1:2", "123:456")
        version: Версия файла (опционально)

    Returns:
        Данные запрошенных нод
    """
    file_key = validate_file_key(file_key)
    node_ids = validate_node_ids(node_ids)
    version = validate_version(version)

    service = FigmaService()
    return await service.get_file_nodes(file_key, node_ids, version=version)
