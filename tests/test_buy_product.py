import time
from pages.cart_page import Cart_page
from pages.catalogue_dogs_page import Dog_page
from pages.dog_food_page import Dog_food_page
from pages.main_page import Main_page



# @pytest.mark.run(order=1)
# def test_byu_filter_product():
#     capabilities = DesiredCapabilities.CHROME.copy()
#     capabilities['pageLoadStrategy'] = 'eager'
#     s = Service('C:\\chromedriver.exe')
#     o = Options()
#     o.add_experimental_option("excludeSwitches", ["enable-logging"])
#     o.add_argument('--ignore-ssl-errors')
#     o.add_argument('--ignore-certificate-errors')
#     driver = webdriver.Chrome(service=s, options=o, desired_capabilities=capabilities)
#
#     print("Start Test")
#
#     mp = Main_page(driver)
#     mp.select_pet_products()
#
#     time.sleep(8)
#     cp = Dog_page(driver)
#     cp.select_dog_catalogue()
#
#     time.sleep(5)
#     dp = Dog_food_page(driver)
#     dp.select_feed_parameters()
#
#     dp.confirmation_order()
#     cartp = Cart_page(driver)
#     cartp.continue_order()
#
#     print("Finish Test")



def test_byu_filter_product(driver):

    print("Start Test")

    mp = Main_page(driver)
    mp.select_pet_products()

    time.sleep(8)
    cp = Dog_page(driver)
    cp.select_dog_catalogue()

    time.sleep(5)
    dp = Dog_food_page(driver)
    dp.select_feed_parameters()

    dp.confirmation_order()
    cartp = Cart_page(driver)
    cartp.continue_order()

    print("Finish Test")

