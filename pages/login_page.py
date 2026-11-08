from playwright.sync_api import Locator, Page


from pages.base_page import BasePage
from utilities import config
import os
from dotenv import load_dotenv
load_dotenv()
class GITHUB_loginPage(BasePage):
    PATH = config.GITHUB_URL

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_username_input(self):
        return self.page.locator('input[name="login"]').fill(os.getenv("TEST_USERNAME"))

    def fill_password_input(self):
        return self.page.locator('input[name="password"]').fill(os.getenv("TEST_PASSWORD"))

    @property
    def sign_in_button(self) -> Locator:
        return self.page.get_by_role("button", name="Sign in", exact=True)