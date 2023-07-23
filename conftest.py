import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service


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
    driver.quit()


