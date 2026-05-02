import pytest
from playwright.sync_api import sync_playwright #, Browser, BrowserContext, Page

@pytest.fixture(scope="session")
def browser(): # -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser): # -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context): # -> Page:
    page = context.new_page()
    yield page
    page.close()

# @pytest.fixture(scope='session')
# def initialize_browser_state(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

#     registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#     registration_email_input.fill('user.name@gmail.com')

#     registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#     registration_username_input.fill('username')

#     registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#     registration_password_input.fill('password')

#     registration_button = page.get_by_test_id('registration-page-registration-button')
#     registration_button.click()

#     context.storage_state(path='browser-state.json')
#     print("[FIXTURE] Контекст сохранился")
#     browser.close()