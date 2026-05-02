import pytest
from playwright.sync_api import sync_playwright, Playwright

@pytest.fixture(scope="session")
def browser(): # -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()



# import pytest
# from playwright.sync_api import Playwright, Page

# # Путь к файлу состояния
# STATE_FILE = "browser-state.json"

# @pytest.fixture
# def browser(): 
#     from playwright.sync_api import sync_playwright
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()

# @pytest.fixture
# def page(browser):
#     page = browser.new_page()
#     yield page
#     page.close()


# @pytest.fixture(scope="session")
# def initialize_browser_state(playwright: Playwright):
#     """
#     Выполняется 1 раз за сессию.
#     Использует фикстуру 'playwright' от плагина.
#     Регистрирует пользователя и сохраняет состояние.
#     """
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()

#     try:
#         print("\n[Init State] Регистрация пользователя...")
#         page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

#         page.get_by_test_id('registration-form-email-input').locator('input').fill('user_email@gmail.com')
#         page.get_by_test_id('registration-form-username-input').locator('input').fill('someUser')
#         page.get_by_test_id('registration-form-password-input').locator('input').fill('password')
        
#         page.get_by_test_id('registration-page-registration-button').click()

#         # Ожидание успешной регистрации
#         page.wait_for_url("**/courses", timeout=15000)
#         print("[Init State] Успешно. Сохранение состояния...")

#         # Сохранение состояния в файл
#         context.storage_state(path=STATE_FILE)
        
#     except Exception as e:
#         print(f"[Init State] Ошибка: {e}")
#         raise e
#     finally:
#         page.close()
#         context.close()
#         browser.close()
#         print("[Init State] Браузер закрыт.\n")


# @pytest.fixture
# def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     # Загружаем сохраненные куки и localStorage
#     context = browser.new_context(storage_state=STATE_FILE)
#     page = context.new_page()
    
#     yield page
    
#     page.close()
#     context.close()
#     browser.close()
