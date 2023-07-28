import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):



    # Locators
    button_continue_no_registration = "//a[@title='Продолжить без регистрации']"
    name_feed = "//a[contains(text(), 'Brit Premium Dog')]"

    # Getters
    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue_no_registration)))

    def get_name_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_feed)))

    # Actions
    def click_button_continue(self):
        self.get_button_continue().click()
        print('Click button continue')

    # Methods

    def continue_order(self):
        """Продолжение заказа"""
        with allure.step('continue_order'):
            Logger.add_start_step(method='continue_order')
            self.click_button_continue()
            self.assert_word(self.get_name_feed(), 'Корм для взрослых собак всех пород Brit Premium Dog Sensitive с '
                                                   'чувствительным пищеварением, с ягненком и идейкой 15 кг')
            Logger.add_end_step(url=self.driver.current_url, method='continue_order')
