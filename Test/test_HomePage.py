import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from Pages.Base import BasePage
from Pages.HomePage import HomePage

driver = webdriver.Chrome("C:\Chromedriver\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)

driver.get("http://alpha-imed.sorsix.com/")


procedure = HomePage(driver)
procedure.click_on_procedure()
procedure.click_on_bodypart()
# procedure.x_on_postcode()
procedure.select_day()
procedure.select_time()
procedure.enter_title()
procedure.firstname()
procedure.lastname()
procedure.DOB()
procedure.DOB_YEAR()
procedure.DOB_MONTH()
procedure.DOB_DAY()
procedure.email()
procedure.confirm_email()
procedure.phone()
procedure.check()
procedure.submit()

# procedure.click_highlight_postcode()
