from configparser import ConfigParser


class ConfigParserHelper:
    def __init__(self):
        self.cfg = ConfigParser()

    def getData(self, section, key):
        self.cfg.read('config\\config.ini')
        return self.cfg.get(section, key)