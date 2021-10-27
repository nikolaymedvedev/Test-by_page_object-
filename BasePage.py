from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PrePage(object):

    def __init__(self, a):
        self.a = a
        self.url = "https://yandex.by/"

    def find_element(self, locator, time=10):
        wait = WebDriverWait(self.a, time)
        element = wait.until(ec.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, time=10):
        wait = WebDriverWait(self.a, time)
        elements = wait.until(ec.presence_of_all_elements_located(locator))
        return elements

    def go_on_url(self):
        go = self.a.get(self.url)
        return go
