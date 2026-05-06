import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
def test_successful_registration(registration_page:RegistationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_page.fill_registration_form(email='ra123@gmail.com', username="SomeUser", password='helloWorld')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_header()

# @pytest.mark.smoke
# def test_disabled_registration_button(page:Page):
#     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

#     registration_button = page.get_by_test_id('registration-page-registration-button')
#     expect(registration_button).to_be_disabled()

#     email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#     email_input.fill('user.name@gmail.com')

#     username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#     username_input.fill('username')

#     password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#     password_input.fill('password')

#     expect(registration_button).not_to_be_disabled()