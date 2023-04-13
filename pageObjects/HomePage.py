from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, " a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    submitForm = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")
    gender = (By.ID, "exampleFormControlSelect1")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getSubmitForm(self):
        return self.driver.find_element(*HomePage.submitForm)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
