import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


# @pytest.fixture()
# def set_up():
#     print('Start test')
#     yield
#     print('Finish test')
#
#
# @pytest.fixture(scope='module')
# def set_group():
#     print('Enter system')
#     yield
#     print('Exit system')

@pytest.fixture(autouse=True, scope="function")
def driver():
    # инициализация браузера
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['pageLoadStrategy'] = 'eager'
    s = Service('C:\\chromedriver.exe')
    o = Options()
    o.add_experimental_option("excludeSwitches", ["enable-logging"])
    o.add_argument('--ignore-ssl-errors')
    o.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service=s, options=o, desired_capabilities=capabilities)

    yield driver

    # завершение работы браузера
    driver.quit()


