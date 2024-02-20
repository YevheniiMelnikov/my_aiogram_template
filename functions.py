from bot.texts.resource_manager import ResourceType, TextManager


def translate(key: ResourceType, lang: str | None = "ua") -> str:
    resource_manager = TextManager()
    return resource_manager.get_text(key, lang)
