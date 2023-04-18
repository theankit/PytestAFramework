import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formBase(self, getData):

        log = self.getlogger()

        homePage = HomePage(self.driver)

        homePage.getName().send_keys(getData["firstName"])
        homePage.getEmail().send_keys(getData["lastName"])
        log.info(getData["firstName"])
        log.info(getData["lastName"])

        homePage.getCheckBox().click()

        # select class provide the methods to handle the options in dropdown
        self.selectOptionFromText(homePage.getGender(), getData["gender"])

        homePage.getSubmitForm().click()

        message = homePage.getSuccessMessage().text
        # log.info(message)
        # print(message)

        assert "Success" in message

        # log.info("Assertion is successful" +message)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
