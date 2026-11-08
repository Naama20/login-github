from pages.login_page import GITHUB_loginPage
from playwright.sync_api import Page, expect

def test_open_login_page(page: Page):
    signInPage = GITHUB_loginPage(page)
    signInPage.open()
    print("Login page opened successfully")
    print("[start] Filling in the username and password fields...")
    signInPage.fill_username_input()
    print("[pass] Username field filled successfully")
    
    print("[start] Filling in the password field...")
    signInPage.fill_password_input()
    print("[pass] Password field filled successfully")
    print("[start] Checking if the sign-in button is visible...")
    signInPage.sign_in_button.is_visible()
    print("[pass] Sign-in button is visible")
