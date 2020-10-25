from selenium import webdriver
from pages.sign_in_auth_page import SignInUpPage

def main():
    browser = webdriver.Chrome()
    signuppage = SignInUpPage(driver=browser) # Don't forget to create the new object
    signuppage.go()
    
    starting_page_title = browser.title

    signuppage.sign_in_email_input.input_text('sammy2@hotmail.com')
    signuppage.sign_in_password_input.input_text('somethin1@..f')
    signuppage.sign_in_button.click()

    test_end_page_title = browser.title

    assert starting_page_title != test_end_page_title
    assert test_end_page_title == "My account - My Store"

    input('Continue? ')
    browser.quit()

main()