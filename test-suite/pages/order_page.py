from .base_elements import BaseElement
from .base_pages import BasePage
from .locator_class import Locator
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    
    url = 'http://automationpractice.com/index.php?controller=history'

    @property
    def continue_checkout_page1(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".standard-checkout > span")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

    @property
    def continue_checkout_page2(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".button:nth-child(4) > span")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

    @property
    def terms_and_conditions_check(self):
        locator = Locator(by=By.XPATH, value="//form[@id='form']/div/p[2]/label")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

    @property
    def continue_checkout_page3(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".standard-checkout > span")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

    @property
    def payment_choice_bank(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".bankwire")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )
    
    @property
    def confirm_order_button(self):
        locator = Locator(by=By.XPATH, value="//p[@id='cart_navigation']/button/span")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

    @property
    def check_order_complete(self):
        locator = Locator(by=By.CSS_SELECTOR, value=".cheque-indent > .dark")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

    @property
    def confirm_order_paragraph(self):
        locator = Locator(by=By.XPATH, value="//div[@id='center_column']/div")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

    @property
    def order_histroy_ID(self):
        locator = Locator(by=By.XPATH, value="//*[@id='order-list']/tbody/tr/td[1]/a")

        return BaseElement(
            driver=self.driver,
            locator=locator,
    )

# proceed_to_checkout_page1 click
# proceed_to_checkout_page2 click
# Click TOC button
# continue -> css=
# click Bankwire Payment
# Click Confirm order
# assert Your order on My Store is complete. TEXT -> css=
# go to -> http://automationpractice.com/index.php?controller=history
# check this text "//*[@id='order-list']/tbody/tr/td[1]/a" == ZCPDKLLCT





