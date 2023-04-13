import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOnce(BaseClass):
    def test_endtoend(self):

        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()

        product_list = checkoutpage.getProdList()
        cardfooterbtn = checkoutpage.getFooterBtn()


        i = -1
        for product in product_list:
            i = i + 1
            product_name = product.text
            print(product_name)
            if product_name == "Blackberry":
                cardfooterbtn[i].click()

        checkoutpage.getCheckoutButton().click()
        asset_text = self.driver.find_element(By.CSS_SELECTOR, "h4[class='media-heading'] a").text
        print(asset_text)
        assert "Blackberry" in asset_text

        confirmOder = checkoutpage.getCheckoutToConfirm()
        confirmOder.getSelectCountry().send_keys("ind")

        self.verifyLinkPresence("India")

        confirmOder.getSelectIndia().click()
        self.driver.find_element(By.LINK_TEXT, "term & Conditions").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-info']").click()
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="checkbox checkbox-primary"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[value="Purchase"]').click()
        success_text = self.driver.find_element(By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]').text
        time.sleep(3)
        print(success_text)
        assert "Thank you!" in success_text
