from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from helium import set_driver, get_driver


def install_webdrivers():
    """Installs the correct selenium webdriver in case the current one is out of date"""
    driver = webdriver.Chrome(ChromeDriverManager(path=".").install())
    set_driver(driver)
    return get_driver()