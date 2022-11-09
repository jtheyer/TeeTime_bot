from robot.api import logger
from selenium import webdriver
import selenium.webdriver.common.desired_capabilities as DC
import platform
import os

class BrowserDriver:
    ''' Do a check for Windows and use appropriate driver.
        This design is aimed at assuming platform operation
        for ease of use. '''
    def attach_chrome_driver():
        curPlatform = platform.platform()
        # Set launch args for Chrome options
        chromeOpts = webdriver.ChromeOptions()
        args = [
            '--disable-web-security',
            # '--disable-application-cache',
            # '--disable-popup-blocking',
            '--disable-save-password-bubble',
            '--allow-insecure-localhost',
            '--remote-debugging-port=9222'
        ]
        for arg in args:
            chromeOpts.add_argument(arg)
        HEADLESS = eval(os.environ.get('HEADLESS', 'False'))    
        if HEADLESS:# ..more launch args
            chromeOpts.add_argument('--headless')
            chromeOpts.add_argument('--disable-gpu')
            
        # CHROME_DEBUGGER_ADDRESS is set in launch.json file. 
        WIN_CHROME_DEBUG = os.environ.get('CHROME_DEBUGGER_ADDRESS', 'WIN_CHROME_DEBUG_notSet')
        if 'Enable' in WIN_CHROME_DEBUG:#assume debug in vscode on Windows Chrome
            chromeOpts.add_experimental_option(
                "debuggerAddress", "localhost:9222")

        # Return a webdriver for the given context 
        if 'Windows' in curPlatform and 'Disable' in WIN_CHROME_DEBUG:#assume docker and vscode
            logger.console('..operating in Docker')
            capabilities = DC.DesiredCapabilities.CHROME.copy()
            capabilities['acceptInsecureCerts'] = True
            driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444', #note: 4444 needs to be added to ports forwarded in VirtualBox
                desired_capabilities=capabilities,
                # options=chromeOpts #! driver appears to not actually use these like it should
            )
            logger.console(f'Desired caps: {driver.desired_capabilities}')
            return driver
        elif 'Windows' in curPlatform:#assume Chrome opened w/ vscode
            logger.console('..operating on windows')
            capabilities = DC.DesiredCapabilities.CHROME.copy()
            capabilities['acceptInsecureCerts'] = True
            # capabilities['goog:loggingPrefs'] = { 'performance':'ALL' }
            cwd = os.getcwd()
            driver = webdriver.Chrome(
                executable_path=f'{cwd}\\src\\bin\\chromedriver.exe',
                desired_capabilities=capabilities,
                options=chromeOpts
            )
            return driver
        elif 'selenium_grid' in os.environ.get('WEBDRIVER'):#assume linux is running Docker Chrome container
            logger.console('..found WEBDRIVER envar......')
            logger.console('..assuming operation is on Linux in Docker Chrome..')
            selenium_grid_host = os.environ.get('SELENIUM_GRID_HOST', 'http://localhost:4444')
            capabilities = DC.DesiredCapabilities.CHROME.copy()
            capabilities['acceptInsecureCerts'] = True
            capabilities['goog:loggingPrefs'] = { 'performance':'ALL' }
            driver = webdriver.Remote(
                command_executor=f'{selenium_grid_host}',
                options=chromeOpts,
                desired_capabilities=capabilities
            )
            return driver
        else:#handle unknown scenario
            logger.console('..! unable to attach webdriver !..')
            logger.console('..!        ..exiting..         !..')
            exit(1)

# if __name__ == "__main__":
#     print(f'executing file --> name: {__name__}')
# else:
#     print(f'importing file --> name: {__name__}')
