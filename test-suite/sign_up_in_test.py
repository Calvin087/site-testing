from selenium import webdriver
from pages.sign_in_auth_page import SignInUpPage

def main():
    browser = webdriver.Chrome()
    signuppage = SignInUpPage(driver=browser) # Don't forget to create the new object
    signuppage.go()
    signuppage.create_account_input.input_text('sammy@hotmail.com')
    signuppage.create_account_button.click()
    signuppage.gender_radio_male.click()


    input('Continue? ')
    browser.quit()

main()