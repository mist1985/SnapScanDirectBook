import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from Locators.Locators import Locators
from Pages.Base import BasePage

class HomePage (BasePage):


    def click_on_procedure(self):
        self.is_visible(Locators.SELECT_SINGLE_PROCEDURE)
        self.click(Locators.SELECT_SINGLE_PROCEDURE)

    def click_on_bodypart(self):
        self.is_visible(Locators.SELECT_BODY_PART)
        self.click(Locators.SELECT_BODY_PART)

    # def enter_postcode(self):
    #     self.is_visible(Locators.POST_CODE)
    #     self.send_postcode(Locators.POST_CODE)

    def x_on_postcode(self):
        self.is_visible(Locators.POST_CODE_PRESS_X)
        self.click(Locators.POST_CODE_PRESS_X)

    def select_day(self):
        self.is_visible(Locators.SELECT_DAY)
        self.click(Locators.SELECT_DAY)

    def select_time(self):
        self.is_visible(Locators.SELECT_TIME)
        self.click(Locators.SELECT_TIME)

    def enter_title(self):
        self.is_visible(Locators.TITLE)
        self.type_title(Locators.TITLE)

    def firstname(self):
        self.is_visible(Locators.FIRST_NAME)
        self.type_name(Locators.FIRST_NAME)

    def lastname(self):
        self.is_visible(Locators.LAST_NAME)
        self.type_surname(Locators.LAST_NAME)

    def DOB(self):
        self.is_visible(Locators.DOB)
        self.click(Locators.DOB)

    def DOB_YEAR(self):
        self.is_visible(Locators.DOB_YEAR)
        self.click(Locators.DOB_YEAR)

    def DOB_MONTH(self):
        self.is_visible(Locators.DOB_MONTH)
        self.click(Locators.DOB_MONTH)

    def DOB_DAY(self):
        self.is_visible(Locators.DOB_DAY)
        self.click(Locators.DOB_DAY)

    def email(self):
        self.is_visible(Locators.EMAIL)
        self.type_email(Locators.EMAIL)

    def confirm_email(self):
        self.is_visible(Locators.CONFIRM_EMAIL)
        self.type_email(Locators.CONFIRM_EMAIL)

    def phone(self):
        self.is_visible(Locators.CONTACT_NUMBER)
        self.type_phone(Locators.CONTACT_NUMBER)

    def check(self):
        self.is_visible(Locators.CHECK_BOX)
        self.click(Locators.CHECK_BOX)

    def submit(self):
        self.is_visible(Locators.BTN_APPOINTMENT)
        self.click(Locators.BTN_APPOINTMENT)


    # def click_highlight_postcode(self):
    #     self.highlight_postcode(Locators.H_POST_CODE)
    #     self.click(Locators.H_POST_CODE)


