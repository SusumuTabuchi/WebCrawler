import json
from datetime import datetime


class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load()

    def load(self):
        try:
            with open(self.config_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return self._create_default_config()

    def save(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=2)

    def get(self, section, key=None):
        if key:
            return self.config.get(section, {}).get(key)
        return self.config.get(section, {})

    def set(self, section, key, value):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value

    def get_timestamp(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")

    def _create_default_config(self):
        return {
            "webdriver": {"width": 1920, "height": 1080},
            "screenshot": {"format": "png", "quality": 80},
            "output": {
                "excel_prefix": "crawl_result",
                "screenshot_prefix": "page_shot",
            },
            "crawler": {"delay": 1, "max_pages": 1000},
        }
