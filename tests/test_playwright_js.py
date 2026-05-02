from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

def test_change_text_with_JS(page:Page):
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login', wait_until='networkidle') # Ждем полной загрузки страницы
     
    # Выполняем JS-код для замены текста заголовка
    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)

