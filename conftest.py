from selenium import webdriver
from pytest import fixture


@fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.get('http://blazedemo.com/')
    driver.maximize_window()
    yield driver

    # Teardown
    print("Travel test completed")
