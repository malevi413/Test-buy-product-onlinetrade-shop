from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Dog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
        self.click_get_dog_food_catalogue()

