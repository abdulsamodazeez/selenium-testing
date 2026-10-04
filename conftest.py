import os
import pytest
from selenium import webdriver

BASE_URL = os.environ["BASE_URL"]
USERNAME = os.environ["APP_USERNAME"]
PASSWORD = os.environ["APP_PASSWORD"]

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.get(BASE_URL)
    yield d
    d.quit()
