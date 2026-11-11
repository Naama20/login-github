from pages.login_page import GITHUB_loginPage
from playwright.sync_api import Page, expect
import os

def test_open_login_page(page: Page, monkeypatch):
    # This checks the form without submitting it, so sample values are sufficient.
    monkeypatch.setenv("TEST_USERNAME", os.getenv("TEST_USERNAME") or "selenium-test-user")
    monkeypatch.setenv("TEST_PASSWORD", os.getenv("TEST_PASSWORD") or "example-password")
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
    
    expect(page.locator('input[name="login"]')).to_have_value(os.environ["TEST_USERNAME"])
    expect(page.locator('input[name="password"]')).to_have_value(os.environ["TEST_PASSWORD"])
    expect(signInPage.sign_in_button).to_be_visible()
    print("[pass] Sign-in button is visible")
