import sys
import os.path

libdir = os.path.dirname(__file__)
sys.path.append(os.path.split(libdir)[0])

import unittest
import allure

from page_objects.onliner import MainPage
from base_test_class import BaseTestClass


class OnlinerBy(BaseTestClass):

    REQUESTED_ITEM = "Наушники HONOR Сhoice Moecen True Wireless Stereo Earbuds CE79"
    SPECIFIC_CATEGORY = "Электроника"
    SPECIFIC_SUBCATEGORY = "Аудиотехника"
    SPECIFIC_ITEMS = "Наушники"

    # Сreate a private method with basic functionality
    def __price_matching(self):
        webpage = MainPage(self.driver)
        webpage.switch_to_frame()
        webpage.input_search_request(self.REQUESTED_ITEM)
        search_price = webpage.get_price_from_search()
        webpage.return_from_frame()
        webpage.go_to_catalogue()
        webpage.go_to_section_page(self.SPECIFIC_CATEGORY)
        webpage.go_to_section_page(self.SPECIFIC_SUBCATEGORY)
        webpage.go_to_items_page(self.SPECIFIC_ITEMS)
        webpage.go_to_specific_item(self.REQUESTED_ITEM)
        item_page_price = webpage.get_price_from_item_page()
        with allure.step("Compare prices"):
            self.assertEqual(search_price, item_page_price), "Prices doesn't match"

    # Test work in a big dislay
    @allure.feature(
        "Matching prices for the same product in the search bar and on its page. "
        "Check in a Big Screen Mode"
    )
    @allure.story(
        "Go to the search bar",
        "Enter a name of the income product and record its price",
        "Go to the product's page and record its price",
        "Compare these prices",
    )
    @allure.severity("major")
    def test_price_matching_big_screen(self):
        self.driver.maximize_window()
        self.__price_matching()

    # Test work in a small dislay
    @allure.feature(
        "Matching prices for the same product in the search bar and on its page. "
        "Check in a Small Screen Mode"
    )
    @allure.story(
        "Go to the search bar",
        "Enter a name of the income product and record its price",
        "Go to the product's page and record its price",
        "Compare these prices",
    )
    @allure.severity("major")
    def test_price_matching_small_screen(self):
        self.driver.set_window_size(400, 660)
        self.__price_matching()


if __name__ == "__main__":
    unittest.main()
