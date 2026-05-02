import os
import pytest
from playwright.sync_api import sync_playwright

STATE_FILE = "browser-state.json"

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def logged_in_context(browser):
    if not os.path.exists(STATE_FILE):
        # Регистрация нового пользователя
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        page.get_by_test_id('registration-form-email-input').locator('input').fill('user.name@gmail.com')
        page.get_by_test_id('registration-form-username-input').locator('input').fill('username')
        page.get_by_test_id('registration-form-password-input').locator('input').fill('password')
        page.get_by_test_id('registration-page-registration-button').click()
        context.storage_state(path=STATE_FILE)
        context.close()
        print("[FIXTURE] Состояние сохранено в", STATE_FILE)
    
    # Возвращаем новый контекст с загруженным состоянием
    context = browser.new_context(storage_state=STATE_FILE)
    yield context
    context.close()

@pytest.fixture
def page(logged_in_context):
    """Создаёт новую страницу в контексте с авторизацией (для каждого теста)."""
    page = logged_in_context.new_page()
    yield page
    page.close()