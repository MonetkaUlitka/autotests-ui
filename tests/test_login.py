from playwright.sync_api import Page, expect 
import pytest
from pages.login_page import LoginPage

@pytest.mark.regression
def test_login_error(login_page:LoginPage, email:str, password:str): 
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_page.login_form.fill(email='user.name@gmail.com', password='password')

    login_page.click_login_button()

    login_page.check_visible_wrong_email_or_password()

@pytest.mark.smoke
def test_hover_registration_link(login_page:LoginPage):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.registration_link.link_hover()