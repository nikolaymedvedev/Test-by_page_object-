from BasePage import PrePage
from selenium.webdriver.common.by import By


class PageObject(PrePage):

    locator_by_field = (By.CSS_SELECTOR, "input[id=text]")
    locator_by_button = (By.CLASS_NAME, "button")
    locator_by_elements = (By.CLASS_NAME, "service__name")

    def write_in_field(self, text):
        find_field = self.find_element(PageObject.locator_by_field, time=8)
        find_field.send_keys(text)
        return find_field

    def click_buttom(self):
        find_button = self.find_element(PageObject.locator_by_button, time=7)
        find_button.click()
        return find_button

    def view_elements(self):
        all_elements = self.find_elements(PageObject.locator_by_elements, time=6)
        elements = [i.text for i in all_elements if len(i.text) > 0]
        return elements
