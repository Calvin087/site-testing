import unittest
from selenium import webdriver
from .pages.sign_in_auth_page import SignInUpPage

class Sign_In_Error(unittest.TestCase):

    def test_Sign_In_Error(self):
        browser = webdriver.Chrome()
        signuppage = SignInUpPage(driver=browser) # Don't forget to create the new object
        signuppage.go()
        
        starting_page_title = browser.title

        signuppage.sign_in_email_input.input_text('sammy2@hotmail.com')
        signuppage.sign_in_password_input.input_text('mywrongpassword') # Incorrect Email
        signuppage.sign_in_button.click()

        assert signuppage.sign_in_error.text == "There is 1 error"

        browser.quit()

if __name__ == '__main__':
    unittest.main()

# Working 2020-10-26 08:09:44