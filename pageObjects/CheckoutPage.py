from selenium.webdriver.common.by import By

from pageObjects.OrderConfirm import ConfirmOrder


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    prodList = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkoutToConfirm = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getProdList(self):
        return self.driver.find_elements(*CheckoutPage.prodList)

    def getFooterBtn(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getCheckoutToConfirm(self):
        self.driver.find_element(*CheckoutPage.checkoutToConfirm).click()
        confirmOder = ConfirmOrder(self.driver)
        return confirmOder

# self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']")