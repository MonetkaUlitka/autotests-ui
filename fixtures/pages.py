import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.registration_page import RegistationPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page:Page) -> RegistationPage:
    return RegistationPage(page=chromium_page)


@pytest.fixture
def dashboard_page(chromium_page:Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)