import time

import pytest

from Pages.CarModelsPage import CarModelsPage
from Pages.HomePage import HomePage
from Pages.NewCarsPage import NewCarsPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider

import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):

    # @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("******Inside New Car Test*********")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(1)

    # @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle",
                             dataProvider.get_data("NewCars"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("******Inside Select Cars Test*********")
        homePage = HomePage(self.driver)
        newCarsPage = NewCarsPage(self.driver)
        carModelsPage = CarModelsPage(self.driver)

        print("Car brand is : ", carBrand)
        if carBrand == "BMW":
            homePage.gotoNewCars()
            newCarsPage.selectBMW()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Hyundai":
            homePage.gotoNewCars()
            newCarsPage.selectHyundai()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Honda":
            homePage.gotoNewCars()
            newCarsPage.selectHonda()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Toyota":
            homePage.gotoNewCars()
            newCarsPage.selectToyota()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"

    def test_selectCars1(self):
        log.logger.info("******Inside Select Cars Test*********")
        homePage = HomePage(self.driver)
        homePage.gotoNewCars()

    @pytest.mark.parametrize("carBrand,carTitle",
                             dataProvider.get_data("NewCars"))
    def test_printCarNamesandPrices(self, carBrand, carTitle):
        log.logger.info("******Inside Car Names and Prices Test*********")
        home = HomePage(self.driver)
        carModelsPage = CarModelsPage(self.driver)
        newCarsPage = NewCarsPage(self.driver)

        print("Car brand is : ", carBrand)
        if carBrand == "BMW":
            home.gotoNewCars()
            newCarsPage.selectBMW()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            carModelsPage.getCarNameAndPrices()
        elif carBrand == "Hyundai":
            home.gotoNewCars()
            newCarsPage.selectHyundai()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            carModelsPage.getCarNameAndPrices()
        elif carBrand == "Honda":
            home.gotoNewCars()
            newCarsPage.selectHonda()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            carModelsPage.getCarNameAndPrices()
        elif carBrand == "Toyota":
            home.gotoNewCars()
            newCarsPage.selectToyota()
            title = carModelsPage.getCarTitle()
            print("Car Title is : " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
            carModelsPage.getCarNameAndPrices()
