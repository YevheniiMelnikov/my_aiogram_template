from enum import Enum, auto

import yaml

import settings


class MessageText(Enum):
    start = auto()

    def __str__(self):
        return f"messages.{self.name}"


class ButtonText(Enum):
    pass

    def __str__(self):
        return f"buttons.{self.name}"


ResourceType = str | MessageText | ButtonText


class TextManager:
    def __init__(self):
        self.messages = self.load_messages()

    def get_text(self, key: ResourceType, lang: str | None = "eng") -> str | None:
        if str(key) in self.messages:
            return self.messages[str(key)][lang]
        else:
            raise ValueError(f"Key {key.name} not found in messages.yaml")

    @staticmethod
    def load_messages() -> dict:
        result = {}
        for type, path in settings.MESSAGES.items():
            with open(path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            for key, value in data.items():
                result[f"{type}.{key}"] = value
        return result


resource_manager = TextManager()


def translate(key: ResourceType, lang: str | None = "ua") -> str:
    return resource_manager.get_text(key, lang)
