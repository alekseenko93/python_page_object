import pytest
import requests

from config_parser.ConfigParserHelper import ConfigParserHelper
from pages.GithubLoginPage import GithubLoginHelper as LoginHelper


@pytest.mark.webtest
def test_github_login(browser_init):
    """Define required data"""
    cfg = ConfigParserHelper()
    login_url = cfg.getData('application_env', 'github_login_url')
    login = cfg.getData('valid_credentials', 'login_github')
    password = cfg.getData('valid_credentials', 'password_github')

    login_page = LoginHelper(browser_init, login_url)
    login_page.visit()
    login_page.type_login(login)
    login_page.type_password(password)
    profile_page = login_page.click_login_button()
    repo_text = profile_page.check_login()
    assert repo_text == 'alekseenko93/python_page_object'


@pytest.mark.api
def test_api_reqres():
    # response_get_users = requests.get('https://reqres.in/api/users?page=2')
    # assert response_get_users.status_code == 200
    # print(f'Response is {response_get_users.text}')

    # json_create_user = {"name": "morpheus", "job": "leader"}
    # response_post_create_user = requests.post('https://reqres.in/api/users', json=json_create_user)
    # assert response_post_create_user.status_code == 201
    # print(f'Response is {response_post_create_user.text}')

    cfg = ConfigParserHelper()
    email = cfg.getData('valid_credentials', 'reqres_email')
    password = cfg.getData('valid_credentials', 'reqres_password')
    json_login_creds = {"email": email, "password": password}
    response_login = requests.post('https://reqres.in/api/register', data=json_login_creds)
    assert response_login.status_code == 200
    print(f'Response is {response_login.text}')
    token = response_login.json()["token"]
    print(f'Token is {token}')
