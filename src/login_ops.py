from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from omnipresent import Omnipresent

class LoginOpsSelectors:
    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password'
    LOGIN_BTN = 'login'


class LoginOps:
    '''Login Operations'''
    driver = Omnipresent.driver
    wait = WebDriverWait(driver, 3)

    def enter_email(email:str):
        '''Enter the given email.'''
        Omnipresent.log(f'entering email.... {email}')
        # skip if not on /login endpoint
        if '/book/search' in LoginOps.driver.current_url:
            return
        el = LoginOps.wait.until(EC.presence_of_element_located(
            (By.NAME, 'email')
        ), f'{__class__} failed to find email input element')
        ActionChains(LoginOps.driver).pause(.2).click(el).pause(.2)\
            .key_down(Keys.LEFT_CONTROL).key_down('a').pause(.2)\
                .key_up(Keys.LEFT_CONTROL).key_up('a').send_keys(Keys.BACKSPACE)\
                    .pause(.2).send_keys(email).pause(.2).perform()

    def enter_pw(pw:str):
        '''Enter the given password.'''
        Omnipresent.log(f'entering pw.... {pw}')
        # skip if not on /login endpoint
        if '/book/search' in LoginOps.driver.current_url:
            return
        el = LoginOps.wait.until(EC.presence_of_element_located(
            (By.NAME, 'password')
        ), f'{__class__} failed to find password input element')
        ActionChains(LoginOps.driver).pause(.2).click(el).pause(.2)\
            .key_down(Keys.LEFT_CONTROL).key_down('a').pause(.2)\
                .key_up(Keys.LEFT_CONTROL).key_up('a').send_keys(Keys.BACKSPACE)\
                    .pause(.2).send_keys(pw).pause(.2).perform()

    def press_login():
        '''Press the "Log-in" button.'''
        Omnipresent.log(f'Press the "Log-in" button.')
        # skip if not on /login endpoint
        if '/book/search' in LoginOps.driver.current_url:
            return
        btn_list = LoginOps.wait.until(EC.presence_of_all_elements_located(
            (By.TAG_NAME, 'button')
        ), f'{__class__} failed to find buttons (for "Log-in")')
        for e in btn_list:
            label = e.get_attribute("innerText")
            if 'Ingresar' in label:
                return ActionChains(LoginOps.driver).pause(.2).click(e).pause(.2).perform()
                