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