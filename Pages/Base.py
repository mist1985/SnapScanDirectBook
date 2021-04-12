import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from Locators import Locators

class BasePage():
    """Define functionalities."""

    # This function is called every time a new object of the base class is created.
    def __init__(self, driver):
         self.driver=driver

    # This function performs a click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).click()
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()


        # This function checks if the web element is visible or not
    # Returns true or false depending upon its visibility. Hence bool.

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def type_title(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys("Mr")

    def type_name(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys("Mihajlo")

    def type_surname(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys("Python")

    def type_email(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys("mihajlo.stojanovski@sorsix.com")

    def type_phone(self, by_locator):
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(
            "1234567890")

    def send_postcode(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys("3000 MELBOURNE")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(Keys.ENTER)


    # def highlight_postcode(self, by_locator):
    #      WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).click("3000 MELBOURNE")
