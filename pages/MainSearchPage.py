from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainSearchLocators:
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    RESULTS_STATS_GOOGLE = (By.ID, 'result-stats')


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(MainSearchLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(MainSearchLocators.SEARCH_BUTTON, time=2).click()

    def get_result_stats_text(self):
        element = self.find_element(MainSearchLocators.RESULTS_STATS_GOOGLE, time=2)
        return element.text
