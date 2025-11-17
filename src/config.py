from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    base_url: str
    page_load_timeout: int


def get_settings():
    return Settings(
        base_url=os.getenv("BASE_URL", "https://qa-scooter.praktikum-services.ru"),
        page_load_timeout=int(os.getenv("PAGE_LOAD_TIMEOUT", "30")),
    )