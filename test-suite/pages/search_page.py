from .base_elements import BaseElement
from .base_pages import BasePage
from .locator_class import Locator
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    url = 'http://automationpractice.com/index.php'

    # Start home page then search.

    @property
    def search_box(self):
        locator = Locator(by=By.ID, value='search_query_top')

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def search_box_button(self):
        locator = Locator(by=By.XPATH, value='//button[@name="submit_search"]')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def first_item_img(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.product_img_link > .replace-2x')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def product_page_buy_button(self):
        locator = Locator(by=By.XPATH, value="//button[@name='Submit']")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )
    
    @property
    def product_page_price(self):
        locator = Locator(by=By.CSS_SELECTOR, value="span#our_price_display")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def added_to_cart_overlay(self):
        locator = Locator(by=By.XPATH, value="//div[@id='layer_cart']/div/div/h2")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def added_to_cart_overlay_exit(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".cross")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def cart_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".shopping_cart > a")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )
    
    @property
    def cart_page_total(self):
        locator = Locator(by=By.ID, value="total_product")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def find_item1_ID(self):
        locator = Locator(by=By.ID, value="product_2_7_0_0")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )
    
    @property
    def find_item2_ID(self):
        locator = Locator(by=By.ID, value="product_1_1_0_0")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    # @property
    # def cart_item_list_first(self):
    #     locator = Locator(by=By.CSS_SELECTOR, value=".first_item .cart_block_product_name")

    #     return BaseElement(
    #         driver=self.driver,
    #         locator=locator,
    #     )

    # @property
    # def cart_item_list_last(self):
    #     locator = Locator(by=By.CSS_SELECTOR, value=".last_item .cart_block_product_name")

    #     return BaseElement(
    #         driver=self.driver,
    #         locator=locator,
    #     )

