import time
from pages.cart_page import Cart_page
from pages.catalogue_dogs_page import Dog_page
from pages.dog_food_page import Dog_food_page
from pages.main_page import Main_page
import allure


@allure.description('Test buy filter product')
def test_buy_filter_product(driver):

    print("Start Test_1")

    mp = Main_page(driver)
    mp.select_pet_products()

    time.sleep(6)
    cp = Dog_page(driver)
    cp.select_dog_catalogue()

    time.sleep(7)
    dp = Dog_food_page(driver)
    dp.select_feed_parameters()

    time.sleep(5)
    dp.confirmation_order()
    cart_p = Cart_page(driver)
    cart_p.continue_order()

    print("Finish Test_1")

