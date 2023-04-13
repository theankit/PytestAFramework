from selenium.webdriver.common.by import By


class ConfirmOrder:
    def __init__(self, driver):
        self.driver = driver

    selectCountry = (By.ID, "country")
    selectIndia = (By.LINK_TEXT, "India")

    def getSelectCountry(self):
        return self.driver.find_element(*ConfirmOrder.selectCountry)

    def getSelectIndia(self):
        return self.driver.find_element(*ConfirmOrder.selectIndia)
