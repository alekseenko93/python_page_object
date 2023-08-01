import pytest

from pages.MainSearchPage import SearchHelper


def test_yandex(browser_init):
    main_page = SearchHelper(browser_init)
    main_page.visit()
    main_page.enter_word("Hello")
    main_page.click_on_the_search_button()
    text = main_page.get_result_stats_text()
    expected_string = 'Результатов: примерно'
    result = expected_string in text
    print("Expected string found") if result else pytest.fail("Expected string NOT found")