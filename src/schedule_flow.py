from random import randint
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from omnipresent import Omnipresent

class ScheduleFlow:
    '''Functions to schedule a tee time.'''
    driver = Omnipresent.driver
    # wait = Omnipresent.wait
    wait = WebDriverWait(driver, 10)

    def select_country():
        '''Will need to ensure chile is selected on first navigation.'''
        Omnipresent.log('..selecting country..')
        el_list = ScheduleFlow.wait.until(EC.visibility_of_all_elements_located(
            (By.TAG_NAME, 'a')
        ), f'{__class__} failed to find <i> elements (country selection)')
        for e in el_list:
            txt = e.get_attribute("innerText")
            if "Chile" in txt:
                ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform() 

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
        ScheduleFlow.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.loadingOverlay[style="display: none;"]')
            ), f'{__class__} failed to find invisibility of loadingOverlay')
        e = ScheduleFlow.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'img[src="https://easycancha-images.s3.amazonaws.com/sports/images/c453148cddc0ec34eefbffe8018cd093.png"]')
        ), f'{__class__} failed to find Golf element')
        # body_div = Omnipresent.driver.find_element(By.TAG_NAME, 'body')
        # ActionChains(ScheduleFlow.driver).pause(.2).click(body_div).pause(.3).perform()
        ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform()
        # el_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
        #     (By.CSS_SELECTOR, 'div.ng-binding') #not a great selector but use this on larger screen size.
        # ), f'{__class__} failed to find Golf element')
        # for i,e in enumerate(el_list):
        #     txt = e.get_attribute("innerText")
        #     if "Golf" in txt:
        #         body_div = Omnipresent.driver.find_element(By.TAG_NAME, 'body')
        #         ActionChains(ScheduleFlow.driver).pause(.2).click(body_div).pause(.3).perform()
        #         ActionChains(ScheduleFlow.driver).pause(.2).click(i+1).pause(.2).perform()
        #         return 

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

    def select_a_time(options: str, selection: str):
        '''Select the desired tee time.'''
        Omnipresent.log(f'Selected time: {selection}')
        el_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'div.hour_item')
        ), f'{__class__} failed to find Time elements. It`s likely there are no times \
available or you have already booked a time for this date.')
        for e in el_list:
            el_time = e.get_attribute("innerText")
            if selection.strip() in el_time:
                return ActionChains(ScheduleFlow.driver).pause(.2).click(e).pause(.2).perform()

    def press_next_btn():
        '''Press the "Next" button.'''
        el = ScheduleFlow.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a.btn-success')
        ), f'{__class__} failed to find success "Siguiente" button')
        ActionChains(ScheduleFlow.driver).pause(.2).click(el).pause(.2).perform()

    def select_mnt_or_valley(subject: str, selection: str):
        '''Select mountain or valley.'''
        Omnipresent.log(f'Selected area: {selection}')
        header_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'div.card_summary_header')
        ), f'{__class__} failed to find mnt or valley header titles')
        found = False
        for i,e in enumerate(header_list):
            txt = e.get_attribute("innerText").lower()[0]
            if selection[0].lower() in txt:
                found = True
                pos = i
        if not found:
            raise AssertionError(f'Selection "{selection}" not found!')
        btn_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'button.btn-success')
        ), f'{__class__} failed to find mnt or valley "Select" buttons"')
        ActionChains(ScheduleFlow.driver).pause(.2).click(btn_list[pos]).pause(.2).perform()

    def press_add_rm_players():
        '''Press the add/remove players button.'''
        ScheduleFlow.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.loadingOverlay[style="display: none;"]')
        ), f'{__class__} failed to find invisibility of loadingOverlay')
        el = ScheduleFlow.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button.btn_level_add_players')
        ), f'{__class__} failed to find "Add/Remove players" button')
        ActionChains(ScheduleFlow.driver).pause(.2).click(el).pause(.2).perform()

    def select_two_players():
        '''Check the box next to 2 players at random.'''
        el_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'div.pointer')
        ), f'{__class__} failed to find player names rows"')
        for e in el_list:
            txt = e.get_attribute("innerText")
            if 'James Hageman' in txt:
                el_list.remove(e)
        rand1 = randint(0,len(el_list)-1)
        rand2 = randint(0,len(el_list)-1)
        while rand2 == rand1:#ensure unique selections
            rand2 = randint(0,len(el_list)-1)
        ScheduleFlow.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.loadingOverlay[style="display: none;"]')
        ), f'{__class__} failed to find invisibility of loadingOverlay')
        ActionChains(ScheduleFlow.driver).pause(.2).click(el_list[rand1]).pause(.2).perform()
        ScheduleFlow.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.loadingOverlay[style="display: none;"]')
        ), f'{__class__} failed to find invisibility of loadingOverlay')
        ActionChains(ScheduleFlow.driver).pause(.2).click(el_list[rand2]).pause(.2).perform()
        ScheduleFlow.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.loadingOverlay[style="display: none;"]')
        ), f'{__class__} failed to find invisibility of loadingOverlay')

    def press_select():
        '''Press the "Seleccionar" button.'''
        el_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'button.btn-success')
        ), f'{__class__} failed to find success buttons (looking for "Seleccionar")')
        for e in el_list:
            txt = e.get_attribute("innerText").lower()
            if 'seleccionar' in txt:
                return ActionChains(ScheduleFlow.driver).click(e).pause(.2).perform()

    def press_book_n_pay_later():
        '''Press the "Book and pay later" button.'''
        ScheduleFlow.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.loadingOverlay[style="display: none;"]')
            ), f'{__class__} failed to find invisibility of loadingOverlay')
        el_list = ScheduleFlow.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'button')
        ), f'{__class__} failed to find "book and pay" buttons')
        for e in el_list:
            txt = e.get_attribute("innerText").lower()
            if 'tarde' in txt:
                Omnipresent.log('..pressing book and pay later!')
                #return ActionChains(ScheduleFlow.driver).click(e).pause(.2).perform()