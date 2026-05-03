import pytest
from playwright.sync_api import sync_playwright, Playwright, expect

@pytest.fixture(scope="session")
def chromium_browser(): # -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# @pytest.fixture
# def context(browser):
#     context = browser.new_context()
#     yield context
#     context.close()

@pytest.fixture
def chromium_page(chromium_browser):
    page = chromium_browser.new_page()
    yield page
    page.close()



@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user_email@gmail.com')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('someUser')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')
    
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    
    yield context.new_page()
    browser.close()
