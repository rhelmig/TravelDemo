from pytest import mark
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# pytest -v -s --html=report.html


# Select departure and arrival
@mark.smoke
@mark.functional
def test_start_page(driver):
    assert driver.title == 'BlazeDemo'
    assert ('Choose your departure city:' in driver.page_source)
    print('text present')


@mark.functional
def test_select_departure_city(driver):
    Select(driver.find_element_by_css_selector(
        'body > div.container > form > select:nth-child(1)')).select_by_visible_text('Boston')


@mark.functional
def test_select_arrival_city(driver):
    Select(driver.find_element_by_css_selector(
        'body > div.container > form > select:nth-child(4)')).select_by_visible_text('Dublin')


@mark.functional
def test_button_find_flights(driver):
    driver.find_element_by_css_selector('input').click()


###################################################################
# Choose a flight
@mark.functional
def test_choose_flight_page_loaded(driver):
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, 'body .container:nth-of-type(2)')))
    assert driver.current_url == 'http://blazedemo.com/reserve.php'
    print('Choose a flight page was loaded')


@mark.functional
def test_choose_a_flight(driver):
    bottom_flight = "tbody tr:nth-of-type(5) [value='Choose This Flight']"
    driver.find_element_by_css_selector(bottom_flight).click()


####################################################################
# Enter User Info
@mark.functional
def test_purchase_page_loaded(driver):
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, "[type='submit']")))
    assert driver.current_url == 'http://blazedemo.com/purchase.php'
    print('Purchase page was loaded')


@mark.functional
def test_user_info_input(driver):
    driver.find_element_by_id('inputName').send_keys('Sam Smith')
    driver.find_element_by_id('address').send_keys('123 Maple St')
    driver.find_element_by_id('city').send_keys('Dacula')
    driver.find_element_by_id('state').send_keys('Georgia')
    driver.find_element_by_id('zipCode').send_keys('30019')


@mark.functional
def test_payment_information(driver):
    Select(driver.find_element_by_id('cardType')).select_by_value('amex')
    driver.find_element_by_id('creditCardNumber').send_keys('432143214321')
    driver.find_element_by_id('creditCardMonth').clear()
    driver.find_element_by_id('creditCardMonth').send_keys('10')
    driver.find_element_by_id('creditCardYear').clear()
    driver.find_element_by_id('creditCardYear').send_keys('2020')
    driver.find_element_by_id('nameOnCard').send_keys('Sam R. Smith')


@mark.functional
def test_remember_me_option(driver):
    driver.find_element_by_id('rememberMe').click()


@mark.functional
def test_purchase_flight_button(driver):
    driver.find_element_by_css_selector("[type='submit']").click()


#######################################################################
# Confirmation page is loaded
@mark.functional
def test_confirmation_page_loaded(driver):
    WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.XPATH, "/html/body//h1[.='Thank you for your purchase today!']")))
    assert driver.current_url == 'http://blazedemo.com/confirmation.php'
    assert ('Thank you for your purchase today!' in driver.page_source)
    print('Flight confirmation confirmed')
