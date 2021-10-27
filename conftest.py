from selenium import webdriver as wb
import pytest


@pytest.fixture(scope="session")
def browser():
    a = wb.Chrome(executable_path=r"C:\Users\nmedvedev\Desktop\Selenium\chromedriver.exe")
    yield a
    a.close()