from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager


class SeleniumWebDriver: 
    def __init__(self,isHeadlessOn:bool=False):
        self.isHeadlessOn=isHeadlessOn

        self.options = webdriver.ChromeOptions()    
        self.options.add_argument('--no-sandbox')   
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_experimental_option('excludeSwitches', ['enable-logging']) #Remove unnecessary logs

        #User Agent
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
        self.options.add_argument(f'user-agent={user_agent}')

        if isHeadlessOn:
            self.options.add_argument('--headless') #Run Webdriver in background            
    
    #forma pratica de utilizar o webdriver
    def _driver(self): 
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=self.options)
        self.driver.implicitly_wait(30)

        return self.driver