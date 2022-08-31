# from random import randint
from robot.api import logger

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# from src.browser_driver import BrowserDriver
from os import getcwd
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class OmnipresentSelectors:
    '''General Selectors that are found in many locations'''
    ADD_btn = 'ion-fab' #.. this is the "+" action button

class Omnipresent:
    def log(msg: str):
        # pass
        logger.console(msg)
    cwd = getcwd()
    log(f'cwd:::::: {cwd}')
    # driver = BrowserDriver.attach_chrome_driver()
    # capabilities = DesiredCapabilities.CHROME.copy()
    chromeOpts = webdriver.ChromeOptions()
    args = [
        '--disable-web-security',
        # '--disable-application-cache',
        # '--disable-popup-blocking',
        '--disable-save-password-bubble',
        '--allow-insecure-localhost',
        '--disable-extensions',
    ]
    for arg in args:
        chromeOpts.add_argument(arg)
    driver = webdriver.Chrome(
        executable_path=f'{cwd}\\src\\bin\\chromedriver.exe',
        # desired_capabilities=capabilities,
        options=chromeOpts
    )
    # driver.implicitly_wait(time_to_wait=3)
    wait = WebDriverWait(driver, 3)
    baseURL = ''

    

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