import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Dog_page(Base):


    # Locators
    dogs_food_button = "//a[@href='/catalogue/korm_dlya_sobak-c1017/']"


    def get_dog_catalogue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dogs_food_button)))

    # Actions
    def click_get_dog_food_catalogue(self):
        self.get_dog_catalogue().click()
        print('Click button dog food catalogue')



    # Methods

    def select_dog_catalogue(self):
        """Выбор категории товары для собак"""
        with allure.step('select_dog_catalogue'):
            Logger.add_start_step(method='select_dog_catalogue')
            self.click_get_dog_food_catalogue()
            Logger.add_end_step(url=self.driver.current_url, method='select_dog_catalogue')

