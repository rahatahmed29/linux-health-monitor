import json
from pathlib import Path


class Config:
    """Load application configuration."""

    def __init__(self):
        config_path = Path(__file__).parent.parent / "configs" / "config.json"

        with open(config_path, "r", encoding="utf-8") as file:
            self.settings = json.load(file)

    def get(self, key):
        return self.settings.get(key)