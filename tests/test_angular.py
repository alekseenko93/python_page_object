import pytest
from pages.AngularSitePage import AngularSiteMainHelper


def test_angular(browser_init):
    main_page = AngularSiteMainHelper(browser_init, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    main_page.visit()
    customer_login_page = main_page.click_customer_login_button()
    url = customer_login_page.get_current_url()
    assert customer_login_page.url == url
