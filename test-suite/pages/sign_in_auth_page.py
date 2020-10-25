from .base_elements import BaseElement
from .base_pages import BasePage
from .locator_class import Locator
from selenium.webdriver.common.by import By

class SignInUpPage(BasePage):

    url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

    # Create Account

    @property
    def create_account_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#email_create')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def create_account_button(self):
        locator = Locator(by=By.ID, value='SubmitCreate')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    # TEST THIS FIRST - Finally Working, now alllllll the elements.

    def gender_radios(self):
        locator = Locator(by=By.ID, value='id_gender1')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )





    # ----------------