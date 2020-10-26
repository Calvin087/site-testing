import unittest
from selenium import webdriver
from .pages.sign_in_auth_page import SignInUpPage
from .pages.search_page import SearchPage
from .pages.order_page import OrderPage

class Confirm_Order_Placed(unittest.TestCase):

    def test_Confirm_Order_Placed(self):
        browser = webdriver.Chrome()
        signuppage = SignInUpPage(driver=browser) # Don't forget to create the new object
        searchpage = SearchPage(driver=browser) # Don't forget to create the new object
        orderpage = OrderPage(driver=browser) # Don't forget to create the new object
        
        signuppage.go()
        
        signuppage.sign_in_email_input.input_text('sammy2@hotmail.com')
        signuppage.sign_in_password_input.input_text('somethin1@..f')
        signuppage.sign_in_button.click()


        find_item1 = "blouse"

        searchpage.search_box.input_text(find_item1)
        searchpage.search_box_button.click()

        searchpage.first_item_img.click()

        find_item1_price = searchpage.product_page_price.text
        

        searchpage.product_page_buy_button.click()
        assert searchpage.added_to_cart_overlay.text == "Product successfully added to your shopping cart", "Product not added correctly"
        searchpage.added_to_cart_overlay_exit.click()

        searchpage.cart_button.click()

        orderpage.continue_checkout_page1.click()
        orderpage.continue_checkout_page2.click()
        orderpage.terms_and_conditions_check.click()
        orderpage.continue_checkout_page3.click()
        orderpage.payment_choice_bank.click()
        orderpage.confirm_order_button.click()

        assert orderpage.check_order_complete.text == "Your order on My Store is complete."

        def order_num_extract(text):
            num = text.rsplit('order reference')[1][1:10]

            return num       

        latest_order_number = order_num_extract(orderpage.confirm_order_paragraph.text)

        orderpage.go()

        assert latest_order_number, "order number not present"

        browser.quit()

if __name__ == '__main__':
    unittest.main()

# Working 2020-10-26 08:16:01