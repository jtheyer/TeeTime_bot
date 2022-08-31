from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.omnipresent import Omnipresent


class ScheduleFlow:
    '''Functions to schedule a tee time.'''
    driver = Omnipresent.driver
    # wait = Omnipresent.wait
    wait = WebDriverWait(driver, 3)

    def select_country():
        '''Will need to ensure chile is selected on first navigation.'''
        Omnipresent.log('........selecting country:::::::')
        el_list = ScheduleFlow.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, 'i')
        ), f'{__class__} failed to find <i> elements (country selection)')
        Omnipresent.log(el_list)
        for e in el_list:
            Omnipresent.log(e)
            Omnipresent.log(e.get_attribute("innerHTML"))
            # if "Club Las Brisas de Chicureo" in e.get_attribute("innerText"):
            #     ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform() 

    def press_pref_clubs():
        '''Click the "My preferred clubs" <article>.'''
        el = ScheduleFlow.wait.until(EC.presence_of_element_located(
            (By.TAG_NAME, 'sliderpreferredclubs')
        ), f'{__class__} failed to find sliderpreferredclubs element')
        ActionChains(ScheduleFlow.driver).pause(.2).click(el).pause(.2).perform()

    def press_club_brisas():
        '''Click the Las Brisas club located under "My preferred clubs".'''
        el = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'p.fvc_name')
        ), f'{__class__} failed to find <p> Las Brisas under preferred clubs')
        for e in el:
            if "Club Las Brisas de Chicureo" in e.get_attribute("innerText"):
                ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform() 

    def press_sport_golf():
        '''Click the "Golf" sport.'''
        e = ScheduleFlow.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'img[src="https://easycancha-images.s3.amazonaws.com/sports/images/c453148cddc0ec34eefbffe8018cd093.png"]')
        ), f'{__class__} failed to find Golf element')
        ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform() 

    def select_today_or_tmro(options: str, selection: str):
        '''Select today or tomorrow.'''
        el_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'div.cds-day')
        ), f'{__class__} failed to find Date (today/tmro) elements')
        try:
            if 'hoy' in selection.lower().strip():
                ActionChains(ScheduleFlow.driver).pause(.2).click(el_list[0]).pause(.2).perform()
            elif 'manana' in selection.lower().strip():
                ActionChains(ScheduleFlow.driver).pause(.2).click(el_list[1]).pause(.2).perform()
            else:
                raise ValueError('Selection must be "hoy" or "manana".')
        except IndexError:
            raise IndexError('index out of range; Today or Tomorrow selected but only one is available.')
        # for e in el_list:
        #     Omnipresent.log(e.get_attribute("innerText"))
            # if "" in e.get_attribute("innerText"):
            #     ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform() 


    def select_a_time(options: str, selection: str):
        '''Select the desired tee time.'''
        Omnipresent.log(f'SELECTED:::: {selection}')
        el_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'div.hour_item')
        ), f'{__class__} failed to find Time elements. It`s likely there are no times \
available or you have already booked a time for this date.')
        for e in el_list:
            Omnipresent.log(e.get_attribute("innerText"))
            el_time = e.get_attribute("innerText")
            if selection.strip() in el_time:
                ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform()
                return