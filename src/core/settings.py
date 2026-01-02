import logging
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Настройки приложения для работы с Figma API."""

    APP_NAME: str = Field(default="Figma MCP Server", description="Название приложения")

    FIGMA_ACCESS_TOKEN: str = Field(default="", description="Персональный токен доступа Figma")
    FIGMA_API_BASE_URL: str = Field(
        default="https://api.figma.com/v1",
        description="Базовый URL для Figma API",
    )

    PORT: int = Field(default=8002, ge=1024, le=65535, description="Порт для запуска MCP сервера")
    HOST: str = Field(default="0.0.0.0", description="Хост для запуска MCP сервера")
    LOG_LEVEL: str = Field(default="INFO", description="Уровень логирования")

    REQUEST_TIMEOUT: int = Field(
        default=60,
        ge=5,
        le=300,
        description="Таймаут запросов к Figma API в секундах",
    )
    IMAGE_SCALE: float = Field(
        default=2.0,
        ge=0.01,
        le=4.0,
        description="Масштаб экспортируемых изображений",
    )
    IMAGE_FORMAT: str = Field(
        default="png",
        description="Формат экспортируемых изображений (png, jpg, svg, pdf)",
    )

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

    def validate_required_fields(self) -> None:
        """Проверка обязательных полей."""
        if not self.FIGMA_ACCESS_TOKEN:
            raise ValueError("FIGMA_ACCESS_TOKEN is required")

    @property
    def headers(self) -> dict[str, str]:
        """Заголовки для API запросов."""
        return {"X-Figma-Token": self.FIGMA_ACCESS_TOKEN}


@lru_cache()
def get_settings() -> Settings:
    """Получить экземпляр настроек (с кешированием)."""
    return Settings()


def setup_logging(level: str = "INFO") -> logging.Logger:
    """Настройка логирования."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    return logging.getLogger("mcp_figma")
