from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config_parser.ConfigParserHelper import ConfigParserHelper


class BasePage:
    cfg = ConfigParserHelper()
    base_url = cfg.getData('application_env', 'url')

    def __init__(self, driver, url=base_url):
        self.url = url
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def visit(self):
        return self.driver.get(self.url)

    def get_current_url(self):
        return self.url
