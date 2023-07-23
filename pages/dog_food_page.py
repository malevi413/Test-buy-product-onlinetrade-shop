from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Dog_food_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    feed_in_stock = "//label[@id='l5950a4a1de00bc24202c5f78a0a726be']/span"
    dry_feed_type_checkbox = "//*[@id='lf87eb6d8d8fcc9377e0af4684857fe7e']/span[1]"
    lamb_taste = "//*[@id='l76e2f3e08e49734976bebec8d2e1a958']/span[1]"
    min_weight_feed = "//input[@id='ves_korma1']"
    max_weight_feed = "//input[@id='ves_korma2']"
    pick_up_button = "//a[@title='Подобрать']"
    sorting_button = "//*[@id='js__listingSort_ID']"
    sorting_desc = "//*[@ value='price-desc']"
    result_filter = "//a[@title='Показать товары по выбранным условиям']"
    name_feed = "//*[@id='l952a042009e252ec0ff4724a113e2fcb']/span[1]"
    button_selected_feed = "//*[@title='Купить Корм для взрослых собак всех пород Brit Premium Dog Sensitive с " \
                           "чувствительным пищеварением, с ягненком и идейкой 15 кг'] "
    button_confirmation_order = "//a[@title='Оформить заказ']"

    def get_feed_in_stock(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.feed_in_stock)))

    def get_dry_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dry_feed_type_checkbox)))

    def get_lamb_taste_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lamb_taste)))

    def get_min_weight_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_weight_feed)))

    def get_max_weight_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_weight_feed)))

    def get_name_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_feed)))

    def get_pick_up_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_button)))

    def get_sorting_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_button)))

    def get_sorting_desc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sorting_desc)))

    def get_result_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.result_filter)))

    def get_button_selected_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_selected_feed)))

    def get_confirmation_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_confirmation_order)))

    # Actions
    def click_feed_in_stock(self):
        self.get_feed_in_stock().click()
        print('Choose feed in stock')

    def click_dry_feed(self):
        self.get_dry_feed().click()
        print('Choose dry feed')

    def click_lamb_taste(self):
        self.get_lamb_taste_feed().click()
        print('Choose lamb')

    def choose_min_weight_feed(self):
        self.get_min_weight_feed().clear()
        self.get_min_weight_feed().send_keys('14999')
        print('Send min weight feed')

    def choose_max_weight_feed(self):
        self.get_max_weight_feed().clear()
        self.get_max_weight_feed().send_keys('15001')
        print('Send max weight feed')

    def click_name_feed(self):
        self.get_name_feed().click()
        print('Choose name')

    def click_pick_up(self):
        self.get_pick_up_button().click()
        print('Click pick up button')

    def click_sorting(self):
        self.get_sorting_button().click()
        print('Click sorting button')

    def click_sorting_desc(self):
        self.get_sorting_desc().click()
        print('Choose sorting desc')

    def confirm_result_filter(self):
        self.get_result_filter().click()
        print('Confirm filters')

    def click_button_selected_feed(self):
        self.get_button_selected_feed().click()
        print('Click button selected feed')

    def click_confirmation_order(self):
        self.get_confirmation_order().click()
        print('Сonfirmation order')

    # Methods
    # def sorting_goods(self):
    #     self.click_sorting()
    #     self.click_sorting_desc()

    def select_feed_parameters(self):
        self.click_feed_in_stock()
        self.click_dry_feed()
        self.click_lamb_taste()
        self.choose_min_weight_feed()
        self.choose_max_weight_feed()
        self.click_name_feed()
        self.confirm_result_filter()

    def confirmation_order(self):
        self.click_button_selected_feed()
        self.click_confirmation_order()
