from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page
import re


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_button = Button(page, locator="registration-page-registration-button", name="Registration button")
        self.login_link = Link(page, locator="registration-page-login-link", name="Login link")


        self.registration_form = RegistrationFormComponent(page)


    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile('.*/#/auth/login'))


