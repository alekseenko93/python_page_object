import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию"""


@pytest.fixture(scope="session")
def browser_init():
    service = Service(executable_path="../chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()