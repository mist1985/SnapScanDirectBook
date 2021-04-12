from selenium import webdriver

from selenium.webdriver.common.by import By


class Locators:
    # HOME PAGE Locators

    # SINGLE PROCEDURE SELECTOR - set to Ultrasound
    SELECT_SINGLE_PROCEDURE = (By.XPATH, "//span[contains(.,'Ultrasound')]")

    # SELECT BODY PART - set to Head

    SELECT_BODY_PART = (By.XPATH, "//span[contains(.,'Head')]")

    # POST CODE - Entering postcode

    POST_CODE = (By.XPATH,"xpath=//input[@id='postCode']")

    # POST CODE CONTAINER PRESS X - There is a popup window that requires the user to enter post code or just click X
    POST_CODE_PRESS_X = (By.XPATH, "//span[contains(.,'×')]")

    # SELECT DAY - Selecting Wednesday as a day to do the testing. Today/Tomorrow might have an issue.

    SELECT_DAY = (By.XPATH,"//a[contains(text(),'Wed')]")

    # SELECT TIME - Select the first timeslot in the table
    SELECT_TIME = (By.CSS_SELECTOR,".time-slot:nth-child(1) .span-link")

    # TITLE - Mr/Mrs
    TITLE = (By.XPATH, "//select[@id='title']")

    # FIRST NAME
    FIRST_NAME = (By.ID, "firstName")

    # LAST NAME
    LAST_NAME = (By.ID, "lastName")

    #DOB - Opens up the calendar
    DOB = (By.CSS_SELECTOR,".svg-icon-calendar > svg")

    # DOB YEAR - Selects the first year
    DOB_YEAR = (By.CSS_SELECTOR, ".dl-abdtp-active")

    # DOB_MONTH - Selects first year (1970)
    DOB_MONTH = (By.XPATH, "//div[2]/div/div")

    # DOB_DAY - Sixth day in the column
    DOB_DAY = (By.XPATH,"//div[6]/div[6]")

    # EMAIL

    EMAIL = (By.ID, 'email')

    # CONFIRM EMAIL
    CONFIRM_EMAIL = (By.ID, 'email_confirm')

    # CONTACT NUMBER
    CONTACT_NUMBER = (By.ID, 'contactNumber')

    # UPLOAD
    UPLOAD = (By.XPATH,
              "/html/body/app-root/ng-component/div/app-map-container/ng-component/div/box/div/div[2]/booking-form/div/form/div/upload-document/div/div[2]/form/div[1]/label")

    # CHECKBOX
    CHECK_BOX = (By.CSS_SELECTOR,".check")

    # BUTTON APPOINTMENT
    BTN_APPOINTMENT = (By.XPATH,
                       "/html/body/app-root/ng-component/div/app-map-container/ng-component/div/box/div/div[2]/booking-form/div/form/div/div[9]/div[3]")

