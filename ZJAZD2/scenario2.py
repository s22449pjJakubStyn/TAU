import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options as chop
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edg

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info('Start of the test scenario')

DRIVER_NAMES = ['Chrome', 'Edge']
for driver_name in DRIVER_NAMES:
    if 'Chro' in driver_name:
        logger.info(f'Starting test with {driver_name} browser')
        chrome_options = chop()
        driver = webdriver.Chrome(options=chrome_options)
    else:
        logger.info(f'Starting test with {driver_name} browser')
        edge_options = edg()
        driver = webdriver.Edge(options=edge_options)

    driver.get('https://wbijam.pl')
    sleep(2)
    accept_cookies= driver.find_element(By.CLASS_NAME, 'qxOn2zvg.e1sXLPUy ')
    accept_cookies.click()

    element_to_hover_over = driver.find_elements(By.CLASS_NAME, 'dropdown')
    actions = ActionChains(driver)
    actions.move_to_element(element_to_hover_over[2]).perform()
    sleep(3)

    element = driver.find_element(By.CSS_SELECTOR, 'a.sub_link[rel="gleipnir"]')
    element.click()
    logger.info("Transfering into subpage")


    current_url = driver.current_url
    expected_url = 'https://gleipnir.wbijam.pl/'

    if current_url == expected_url:
        logger.info(f'Correct transfer to the appropriate subpage = {current_url}')
    else:
        logger.info(f'Incorrect transfer to the appropriate subpage. You should be on {expected_url}')

    logger.info(f'End of the test scenario2 for {driver_name} browser')
    driver.close()