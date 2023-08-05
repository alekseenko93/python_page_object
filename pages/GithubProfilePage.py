from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class GithubProfilePageSelectors:
    REPOSITORY_LINK = (By.LINK_TEXT, "alekseenko93/python_page_object")


class GithubProfilePage(BasePage):

    def check_login(self):
        element = self.find_element(GithubProfilePageSelectors.REPOSITORY_LINK, time=5)
        return element.text
