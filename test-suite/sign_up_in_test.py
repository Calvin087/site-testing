from selenium import webdriver
from pages.sign_in_auth_page import SignInUpPage

def main():
    browser = webdriver.Chrome()
    signuppage = SignInUpPage(driver=browser) # Don't forget to create the new object
    signuppage.go()
    
    starting_page_title = browser.title

    signuppage.create_account_input.input_text('sammy2@hotmail.com')
    signuppage.create_account_button.click()
    signuppage.gender_radio_male.click()
    signuppage.form_FirstName.input_text('Samuel')
    signuppage.form_LastName.input_text('El Gato')
    signuppage.form_Password.input_text('somethin1@..f')
    signuppage.dropDown_day(10).select_dropdown()
    signuppage.dropDown_months(5).select_dropdown()
    signuppage.dropDown_years(33).select_dropdown()
    signuppage.form_address1.input_text('Calle Tesoro')
    signuppage.form_city.input_text('Madrid')
    signuppage.dropDown_state(5).select_dropdown()
    signuppage.form_postcode.input_text('28027')
    signuppage.form_mobile.input_text('07716132949')
    signuppage.form_alias_input.input_text('my fake account')
    signuppage.account_register_button.click()

    test_end_page_title = browser.title

    assert starting_page_title != test_end_page_title
    assert test_end_page_title == "My account - My Store"

    input('Continue? ')
    browser.quit()

main()