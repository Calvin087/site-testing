from .locator_class import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        #set this later so i can use the wait.

        self.find()
        # first thing to be called after init

    
    def find(self):
        
        found_element = WebDriverWait(
            self.driver, 10).until( # max 10secs, until
                EC.visibility_of_element_located( # expected Con item located
                    self.locator)) # this item, based on id/class xpath/css selector.

        self.web_element = found_element
        return None

    
    def input_text(self, text):
        self.web_element.send_keys(text) # if it is an input found, send keys bro
        return None

    
    def click(self):

        element = WebDriverWait(
            self.driver, 10).until( # ensure button has loaded
                EC.element_to_be_clickable(self.locator))

        element.click()
        return None

    
    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        # could be useful for debugging too if needed
        return attribute

    @property
    def text(self):
        # strip out text
        text = self.web_element.text
        return text