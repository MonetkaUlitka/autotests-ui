from playwright.sync_api import Page, expect 
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent

class RegistationPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        registration_form = RegistrationFormComponent(page)

        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

       
    def click_registration_button(self):
        self.registration_button.click()
