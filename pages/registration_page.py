from playwright.sync_api import Page, expect 
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.link import Link
from elements.button import Button 

class RegistationPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.registration_form = RegistrationFormComponent(page)

        self.login_link = Link(page, 'registration-page-login-link', 'Login Link')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration Button')

       
    def click_registration_button(self):
        self.registration_button.click()
