from login_ops import LoginOps
from robot.api.deco import keyword
from omnipresent import Omnipresent
from selenium.webdriver.support import expected_conditions as EC
from schedule_flow import ScheduleFlow as SF

ROBOT_AUTO_KEYWORDS = False

@keyword
def navegar_por(url:str, *extraInfo):
    Omnipresent.log(f'..attempting nav to: {url}')
    Omnipresent.driver.get(url)
    Omnipresent.driver.get(url)
    Omnipresent.log(f'window handles::::: {Omnipresent.driver.window_handles}')
    
    #select Chile if/when needed
    try:
        at_country_select = Omnipresent.wait.until(EC.url_contains('/profile/countries'))
        if at_country_select:
            Omnipresent.log('need to select country!!!')
            SF.select_country()
            return
    except:
        Omnipresent.log('navigation except.. passing....')
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
        'Golf': SF.press_sport_golf
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
        'la hora:': SF.select_a_time
    }
    fn = opts.get(subject)
    if extraInfo:
        fn(subject, extraInfo[0])
    else:
        fn()

@keyword
def close_the_browser():
    Omnipresent.driver.quit()