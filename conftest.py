import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser():
    with sync_playwright() as p:
        # Запускаем браузер (headless=False показывает окно)
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    # Создаем новую страницу для каждого теста
    page = browser.new_page()
    yield page
    page.close()