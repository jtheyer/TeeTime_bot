# from random import randint
from robot.api import logger

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

from browser_driver import BrowserDriver

class OmnipresentSelectors:
    '''General Selectors that are found in many locations'''
    ADD_btn = 'ion-fab' #.. this is the "+" action button

class Omnipresent:
    driver = BrowserDriver.attach_chrome_driver()
    driver.implicitly_wait(time_to_wait=3)
    wait = WebDriverWait(driver, 3)
    baseURL = ''

    def log(msg: str):
        # pass
        logger.console(msg)

    ''' Key presses '''
    def tab():
        a = ActionChains(Omnipresent.driver)
        a.key_down(Keys.TAB).key_up(Keys.TAB).perform()

    def enter():
        a = ActionChains(Omnipresent.driver)
        a.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def end():
        a = ActionChains(Omnipresent.driver)
        a.key_down(Keys.END).key_up(Keys.END).perform()