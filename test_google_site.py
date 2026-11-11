import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




@pytest.mark.selenium
def test_google_title(driver):
    assert "Google" in driver.title

def test_google_search(driver):
    element = driver.find_element("name", "q")
    element.send_keys("SOXL stock price")
    element.clear()
    print(element.get_attribute("value"))
    element.submit()
    # element.send_keys(Keys.ENTER)


def test_css(driver):
    driver.set_window_size(800, 800)
    driver.get("https://playwright.dev/")

    button = driver.find_element("css selector", "button[aria-label='Toggle navigation bar']")
    button.click()
    link = driver.find_element(By.XPATH, '//*[@id="__docusaurus"]/nav/div[3]/div[2]/div[1]/ul/li[3]')
    link.click()