from selenium import webdriver
from pages.sign_in_auth_page import SignInUpPage
from pages.search_page import SearchPage

# - Blouse
# - Faded Short Sleeve T-shirts

def main():
    browser = webdriver.Chrome()
    searchpage = SearchPage(driver=browser) # Don't forget to create the new object
    searchpage.go()

    find_item1 = "blouse"
    find_item2 = "Faded Short Sleeve T-shirts"

    searchpage.search_box.input_text(find_item1)
    searchpage.search_box_button.click()

    searchpage.first_item_img.click()

    find_item1_price = searchpage.product_page_price.text
    

    searchpage.product_page_buy_button.click()
    assert searchpage.added_to_cart_overlay.text == "Product successfully added to your shopping cart", "Product not added correctly"
    searchpage.added_to_cart_overlay_exit.click()

    searchpage.cart_button.click()

    assert searchpage.find_item1_ID

    ##

    searchpage.search_box.input_text(find_item2)
    searchpage.search_box_button.click()

    searchpage.first_item_img.click()

    find_item2_price = searchpage.product_page_price.text
    

    searchpage.product_page_buy_button.click()
    assert searchpage.added_to_cart_overlay.text == "Product successfully added to your shopping cart", "Product not added correctly"
    searchpage.added_to_cart_overlay_exit.click()

    searchpage.cart_button.click()

    assert searchpage.find_item1_ID

    #

    add_item_totals = float(find_item1_price[1:]) + float(find_item2_price[1:])
    on_page_cart_total = float(searchpage.cart_page_total.text[1:])

    final_item_totals = "{:.2f}".format(add_item_totals)

    assert float(final_item_totals) == on_page_cart_total

    input('Continue? ')
    browser.quit()

main()