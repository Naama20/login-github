from playwright.sync_api import Locator, Page
import utilities.config as config


class BasePage:
    PATH = config.GITHUB_URL
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.PATH, wait_until="domcontentloaded")