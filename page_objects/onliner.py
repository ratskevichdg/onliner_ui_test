from .base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    SEARH_BOX_ICON = (By.XPATH, '//*[@id="fast-search"]/form/input[1]')
    MODAL_IFRAME = (By.CLASS_NAME, "modal-iframe")
    SEARCH_BOX = (By.XPATH, "//div[@id='search-page']/div[@class='search__bar']//input")
    FIRST_ITEM_PRICE = (
        By.XPATH,
        # ЗАМЕНИ ЭТОТ XPATH!!!!
        '//*[@id="search-page"]/div[2]/ul/li[1]/div/div/div[1]/div/div[1]/a/span',
    )
    CATALOGUE_BUTTON_BIG_SCREEN = (
        By.XPATH,
        '//a[@href="https://catalog.onliner.by/"]/span',
    )
    CATALOGUE_BUTTON_SMALL_SCREEN = (
        By.XPATH,
        # ЗАМЕНИ ЭТОТ XPATH!!!!
        '//*[@id="navigation-sidebar"]/div[2]/div[2]/div[2]/ul[1]/li[2]',
    )
    NAV_SIDEBAR = (By.XPATH, '//*[@id="navigation-sidebar"]/div[2]/a')
    CLOSE_IFRAME_BUTTON = (By.XPATH, '//*[@id="search-page"]/div[1]/span')
    All_CATEGORIES_BUTTON = (
        By.XPATH,
        # ЗАМЕНИ ЭТОТ XPATH!!!!
        '//*[@id="container"]/div/div/div/div/div[1]/div[1]/div[1]',
    )
    PRICE_FROM_SPECIFIC_ITEM_PAGE = (
        By.XPATH,
        "//div[contains(@class,'offers-description__price_primary')]",
    )

    @allure.step("Switch to the iFrame")
    def switch_to_frame(self):
        self.driver.find_element(*self.SEARH_BOX_ICON).click()
        self.driver.switch_to.frame(self.driver.find_element(*self.MODAL_IFRAME))

    @allure.step("Return to the default page")
    def return_from_frame(self):
        if self.driver.get_window_size()["width"] <= 1000:
            self.driver.find_element(*self.CLOSE_IFRAME_BUTTON).click()
        self.driver.switch_to.default_content()

    @allure.step("Input search request with specific item")
    def input_search_request(self, request):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(request)

    @allure.step("Get item's price from pop-up window from search bar")
    def get_price_from_search(self):
        return self.driver.find_element(*self.FIRST_ITEM_PRICE).text

    @allure.step("Go to catalogue")
    def go_to_catalogue(self):
        if self.driver.get_window_size()["width"] > 1000:
            self.driver.find_element(*self.CATALOGUE_BUTTON_BIG_SCREEN).click()
        else:
            self.driver.find_element(*self.NAV_SIDEBAR).click()
            self.driver.find_element(*self.CATALOGUE_BUTTON_SMALL_SCREEN).click()

    @allure.step("Switch to specific section/subsection")
    def go_to_section_page(self, section):
        self.driver.find_element_by_xpath(f"//*[contains(text(),'{section}')]").click()

    @allure.step("Switch to the items catalogue")
    def go_to_items_page(self, section):
        param_page_link = self.driver.find_element_by_xpath(
            f"//span[contains(@class, 'catalog-navigation-list__dropdown-title') and contains(text(), '{section}')]/../.."
        ).get_attribute("href")
        self.driver.get(param_page_link)

    @allure.step("Switch to the specific item page")
    def go_to_specific_item(self, section):
        self.driver.find_element_by_xpath(f"//span[contains(text(),'{section}')]").click()

    @allure.step("Get price from item's page")
    def get_price_from_item_page(self):
        return self.driver.find_element(*self.PRICE_FROM_SPECIFIC_ITEM_PAGE).text
