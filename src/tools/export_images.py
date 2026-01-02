from typing import Optional

from src.core.validators import (
    validate_file_key,
    validate_image_format,
    validate_node_ids,
    validate_scale,
    validate_version,
)
from src.entrypoints.mcp_instance import mcp
from src.services.figma_service import FigmaService


@mcp.tool()
async def export_images(
    file_key: str,
    node_ids: list[str],
    scale: Optional[float] = None,
    format: Optional[str] = None,
    version: Optional[str] = None,
) -> dict:
    """
    Экспортировать изображения нод из файла Figma.

    Args:
        file_key: Ключ файла Figma (из URL)
        node_ids: Список ID нод для экспорта
        scale: Масштаб изображения (0.01-4.0, по умолчанию 2.0)
        format: Формат изображения (png, jpg, svg, pdf)
        version: Версия файла (опционально)

    Returns:
        Словарь с URL изображений для каждой ноды
    """
    file_key = validate_file_key(file_key)
    node_ids = validate_node_ids(node_ids)
    version = validate_version(version)

    if scale is not None:
        scale = validate_scale(scale)
    if format is not None:
        format = validate_image_format(format)

    service = FigmaService()
    return await service.get_images(file_key, node_ids, scale=scale, format=format, version=version)
