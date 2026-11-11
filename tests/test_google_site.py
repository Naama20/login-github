import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse




@pytest.mark.selenium
def test_google_title(driver):
    assert "Google" in driver.title

def test_google_search(driver):
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    element.clear()
    element.send_keys("SOXL stock price")
    element.send_keys(Keys.ENTER)
    WebDriverWait(driver, 15).until(
        lambda browser: urlparse(browser.current_url).path.startswith(("/search", "/sorry"))
    )
    if urlparse(driver.current_url).path.startswith("/sorry"):
        pytest.skip("Google blocked the automated search with a CAPTCHA")
    WebDriverWait(driver, 15).until(EC.title_contains("SOXL stock price"))


def test_css(driver):
    driver.set_window_size(800, 800)
    driver.get("https://playwright.dev/")

    button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[aria-label='Toggle navigation bar']")
    ))
    button.click()
    link = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.navbar-sidebar a[href="/docs/intro"]')
    ))
    link.click()
    WebDriverWait(driver, 15).until(EC.url_contains("/docs/intro"))
