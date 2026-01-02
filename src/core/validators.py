import re
from typing import Optional


def validate_file_key(file_key: str) -> str:
    """Валидация ключа файла Figma."""
    if not file_key or not isinstance(file_key, str):
        raise ValueError("File key is required and must be a string")

    file_key = file_key.strip()
    if not file_key:
        raise ValueError("File key cannot be empty")

    if not re.match(r"^[a-zA-Z0-9_-]+$", file_key):
        raise ValueError("Invalid file key format")

    return file_key


def validate_node_id(node_id: str) -> str:
    """Валидация ID ноды Figma."""
    if not node_id or not isinstance(node_id, str):
        raise ValueError("Node ID is required and must be a string")

    node_id = node_id.strip()
    if not node_id:
        raise ValueError("Node ID cannot be empty")

    if not re.match(r"^[\d:]+$", node_id):
        raise ValueError("Invalid node ID format (expected format: '1:2')")

    return node_id


def validate_node_ids(node_ids: list[str]) -> list[str]:
    """Валидация списка ID нод."""
    if not node_ids:
        raise ValueError("At least one node ID is required")

    return [validate_node_id(nid) for nid in node_ids]


def validate_image_format(format: str) -> str:
    """Валидация формата изображения."""
    valid_formats = ["png", "jpg", "jpeg", "svg", "pdf"]
    format = format.lower().strip()

    if format not in valid_formats:
        raise ValueError(f"Invalid image format. Must be one of: {', '.join(valid_formats)}")

    return format


def validate_scale(scale: float) -> float:
    """Валидация масштаба изображения."""
    if scale < 0.01 or scale > 4.0:
        raise ValueError("Scale must be between 0.01 and 4.0")

    return scale


def validate_version(version: Optional[str]) -> Optional[str]:
    """Валидация версии файла."""
    if version is None:
        return None

    version = version.strip()
    if not version:
        return None

    return version
