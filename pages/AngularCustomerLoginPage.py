from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AngularCLPageLocators:
    CUSTOMER_LOGIN_BTN = (By.CSS_SELECTOR, '[ng-click="customer()"]')


class AngularCLHelper(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_customer_login_button(self):
        self.find_element(AngularCLPageLocators.CUSTOMER_LOGIN_BTN, time=2).click()
        return

    def get_current_url(self):
        return self.driver.current_url
