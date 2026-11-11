

import os

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = options()
    ciENV = os.getenv("CI")
    if ciENV:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    yield driver
    driver.quit()  # runs even if the test fails