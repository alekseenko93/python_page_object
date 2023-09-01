from selenium.webdriver.common.by import By

from pages.AngularCustomerLoginPage import AngularCLHelper
from pages.BasePage import BasePage


class AngularSiteMainPageLocators:
    CUSTOMER_LOGIN_BTN = (By.CSS_SELECTOR, '[ng-click="customer()"]')


class AngularSiteMainHelper(BasePage):

    def click_customer_login_button(self):
        self.find_element(AngularSiteMainPageLocators.CUSTOMER_LOGIN_BTN, time=2).click()
        return AngularCLHelper(self.driver)
