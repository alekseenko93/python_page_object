from pages.AngularSitePage import AngularSiteMainHelper


def test_angular(browser_init):
    home_page = AngularSiteMainHelper(browser_init, 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    home_page.visit()
    customer_login_page = home_page.click_customer_login_button()
    url = customer_login_page.get_current_url()

    assert 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer' == url
