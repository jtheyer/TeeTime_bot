from login_ops import LoginOps
from robot.api.deco import keyword
from omnipresent import Omnipresent
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from schedule_flow import ScheduleFlow as SF

ROBOT_AUTO_KEYWORDS = False

@keyword
def navegar_por(url:str, *extraInfo):
    Omnipresent.log(f'..attempting nav to: {url}')
    Omnipresent.driver.get(url)
    #select Chile if/when needed
    try:
        at_country_select = Omnipresent.wait.until(EC.url_contains('/profile/countries'))
        if at_country_select:
            Omnipresent.log('Need to select country..')
            SF.select_country()
            return
    except:
        pass
    #handle pop up
    try:
        popup_title = Omnipresent.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'h3.modal-title')
        ), 'Keyword "navegar_por" did not find the "new country selection in account" popup')
        if popup_title:
            ok_btn = Omnipresent.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div.modal-footer > button')
            ), 'Keyword "navegar_por" did not find the "Ok" button')
            ActionChains(Omnipresent.driver).pause(.2).click(ok_btn).pause(.2).perform()
    except:
        pass


@keyword
def ingresar(subject:str, *extraInfo):
    if 'email' in subject or 'clave' in subject:
        parts = subject.split(':')
        subject = parts[0].strip()
        value = parts[-1].strip()
    opts = {
        'email': LoginOps.enter_email,
        'clave': LoginOps.enter_pw
    }
    fn = opts.get(subject)
    if value:
        fn(value)
    else:
        fn()

@keyword
def apreton(subject:str, *extraInfo):
    opts = {
        'Login': LoginOps.press_login,
        'preferred clubs': SF.press_pref_clubs,
        'club brisas': SF.press_club_brisas,
        'Golf': SF.press_sport_golf,
        'Siguiente': SF.press_next_btn,
        'Agregar/Quitar jugadores': SF.press_add_rm_players,
        'Seleccionar': SF.press_select,
        'Reservar y pagar mas tarde': SF.press_book_n_pay_later
    }
    fn = opts.get(subject)
    if extraInfo:
        fn(subject, extraInfo[0])
    else:
        fn()

@keyword
def Escoja(subject:str, *extraInfo):
    opts = {
        'hoy o manana?': SF.select_today_or_tmro,
        'la hora:': SF.select_a_time,
        'montana o valle?': SF.select_mnt_or_valley,
        '2 jugadores': SF.select_two_players
    }
    fn = opts.get(subject)
    if extraInfo:
        fn(subject, extraInfo[0])
    else:
        fn()

@keyword
def close_the_browser():
    Omnipresent.driver.quit()