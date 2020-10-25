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

    @property
    def gender_radio_male(self):
        locator = Locator(by=By.CSS_SELECTOR, value='.radio-inline:nth-child(3) > .top')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )

    @property
    def form_FirstName(self):
        locator = Locator(by=By.ID, value='customer_firstname')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )
    
    @property
    def form_LastName(self):
        locator = Locator(by=By.ID, value='customer_lastname')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )
    
    # def form_Email(self): - page autocompletes this, maybe don't mess with it.
    #     locator = Locator(by=By.CSS_SELECTOR, value='//input[@id= "email"]')

    #     return BaseElement(
    #         driver=self.driver,
    #         locator=locator,
    #     )
    
    @property
    def form_Password(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#passwd')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )


    def dropDown_day(self, index):
        locator = Locator(by=By.XPATH, value=f"//select[@id='days']/option[{index}]")

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )


    def dropDown_months(self, index):
        locator = Locator(by=By.XPATH, value=f"//select[@id='months']/option[{index}]")

        return BaseElement(
            driver=self.driver,
            locator=locator
        )


    def dropDown_years(self, index):
        locator = Locator(by=By.XPATH, value=f"//select[@id='years']/option[{index}]")

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def form_address1(self):
        locator = Locator(by=By.ID, value='address1')

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def form_city(self):
        locator = Locator(by=By.ID, value='city')

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def dropDown_state(self, index):
        locator = Locator(by=By.XPATH, value=f"//select[@id='id_state']/option[{index}]")

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def form_postcode(self):
        locator = Locator(by=By.ID, value='postcode')

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def form_mobile(self):
        locator = Locator(by=By.ID, value='phone_mobile')

        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def form_alias_input(self):
        locator = Locator(by=By.ID, value='alias')

        return BaseElement(
            driver=self.driver,
            locator=locator
        )


    @property
    def account_register_button(self):
        locator = Locator(by=By.ID, value='submitAccount')

        return BaseElement(
            driver=self.driver,
            locator=locator,
        )