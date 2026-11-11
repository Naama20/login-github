

import os

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    ciENV = os.getenv("CI")
    if ciENV and ciENV.lower() not in {"false", "0"}:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.google.com")
        yield driver
    finally:
        driver.quit()
