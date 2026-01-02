import sys

from src.core.settings import get_settings, setup_logging
from src.entrypoints.mcp_instance import mcp


def main():
    """Запуск MCP сервера."""
    settings = get_settings()
    logger = setup_logging(settings.LOG_LEVEL)

    from src.tools import (  # noqa: F401
        export_images,
        get_comments,
        get_components,
        get_file,
        get_file_nodes,
        get_project_files,
        get_styles,
        get_team_projects,
    )

    try:
        settings.validate_required_fields()
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)

    logger.info(f"Starting {settings.APP_NAME} on {settings.HOST}:{settings.PORT}")

    mcp.run(transport="sse", host=settings.HOST, port=settings.PORT)


if __name__ == "__main__":
    main()
