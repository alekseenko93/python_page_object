from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.GithubProfilePage import GithubProfilePage


class GithubLoginPageSelectors:
    LOGIN_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "commit")


class GithubLoginHelper(BasePage):

    def type_text(self, selector, text):
        input_field = self.find_element(selector)
        input_field.send_keys(text)
        return input_field

    def type_login(self, text):
        return self.type_text(GithubLoginPageSelectors.LOGIN_FIELD, text)

    def type_password(self, text):
        return self.type_text(GithubLoginPageSelectors.PASSWORD_FIELD, text)

    def click_login_button(self):
        self.find_element(GithubLoginPageSelectors.LOGIN_BUTTON, time=2).click()
        return GithubProfilePage(self.driver, 'https://github.com/')
