from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

driver = None

@given('I open the website "{url}" using "{browser}" browser')
def open_website(context, url, browser):
    print(browser)
    global driver
    options = ChromeOptions() if 'chrome' in browser.lower() else EdgeOptions()
    context.driver = webdriver.Chrome(options=options) if 'chrome' in browser.lower() else webdriver.Edge(options=options)
    context.driver.get(url)

@when('I click on accept cookies button')
def click_accept_cookies_button(context):
    context.driver.find_element(By.CLASS_NAME, 'qxOn2zvg.e1sXLPUy ').click()
    sleep(2)

@when('I hover specific dropdown menu')
def hover_dropdown_menu(context):
    element_to_hover_over = context.driver.find_elements(By.CLASS_NAME, 'dropdown')
    actions = ActionChains(context.driver)
    actions.move_to_element(element_to_hover_over[2]).perform()
    sleep(3)

@when('I click specific anime pannel')
def click_anime_subpage(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a.sub_link[rel="gleipnir"]').click()
    sleep(2)

@then('I should be on the correct anime subpage')
def check_current_page(context):
    current_url = context.driver.current_url
    expected_url = 'https://gleipnir.wbijam.pl/'

    if current_url == expected_url:
        logger.info(f'Correct transfer to the appropriate subpage = {current_url}')
    else:
        logger.info(f'Incorrect transfer to the appropriate subpage. You should be on {expected_url}')

    # context.driver.quit()
