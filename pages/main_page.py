from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_catalogue = "//a[@class='header__button header__buttonCatalog  js__catalogLine__mainLink ']"
    pet_products = "//a[@href='/catalogue/zootovary-c1014/']"
    dog_products = "//a[@href='/catalogue/dlya_sobak-c1804/']"
    main_word = "//h1[contains(text(),'Для собак')]"

    # Getters

    def get_button_catalogue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_catalogue)))

    def get_pet_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pet_products)))

    def get_dog_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dog_products)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def click_button_catalogue(self):
        self.get_button_catalogue().click()
        print('Click button catalogue')

    def click_pet_products(self):
        self.get_pet_products().click()
        print('Click pet products')

    def click_dog_products(self):
        self.get_dog_products().click()
        print('Click dog products')

    # Methods
    def select_pet_products(self):
        Logger.add_start_step(method='select_pet_products')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_button_catalogue()
        self.click_pet_products()
        self.click_dog_products()
        self.assert_word(self.get_main_word(), 'Для собак')
        Logger.add_end_step(url=self.driver.current_url, method='select_pet_products')
