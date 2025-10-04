from time import sleep
from os import getenv
from dotenv import load_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class GoDeepBrowser(Chrome):
    
    def __init__(self):
        pass
    
    def _init(self, headless: bool) -> None:
        self._instance_chrome(headless=headless)
        self._login()
    
    def _instance_chrome(self, headless: bool) -> None:
        options = Options()
        options.add_argument(argument="--disable-logging")
        options.add_argument(argument="--log-level=3")
        options.add_argument(argument="--silent")
        options.add_argument(argument="--v=0")
        options.add_experimental_option(name="useAutomationExtension", value=False) # type: ignore
        options.add_experimental_option(name="excludeSwitches", value=["enable-automation", "enable-logging"]) # type: ignore
        if headless:
            options.add_argument(argument="--headless=new")
        else:
            options.add_experimental_option(name="detach", value=True) # type: ignore
        super().__init__(options=options)
    
    def _login(self) -> None:
        load_dotenv()
        self.get(f"https://www.revendedorpositivo.com.br/admin/")
        user = self.find_element(by=By.ID, value="username")
        password = self.find_element(by=By.ID, value="password")
        login_button = self.find_element(by=By.XPATH, value="//div[@id='action-login']/div[@class='col-md-12 pad-right0 pad-left0']/button[@class=' col-md-12 btn btn-primary button-login-home pad-bottom10']")
        user.send_keys(getenv("GODEEP_EMAIL")) # type: ignore
        password.send_keys(getenv("GODEEP_PASSWORD")) # type: ignore
        login_button.click()
        sleep(1)
        body = self.find_element(by=By.TAG_NAME, value="body").text
        if any(login_string in body for login_string in ["Because you're accessing sensitive info, you need to verify your password.", "Sign in", "Pick an account", "Entrar"]):
            print("Necessário logar conta Microsoft.")
            while True:
                body = self.find_element(by=By.TAG_NAME, value="body").text
                if "DASHBOARD" in body:
                    break
                else:
                    sleep(3)
        if "Approve sign in request" in body:
            sleep(1)
            code = self.find_element(by=By.ID, value="idRichContext_DisplaySign").text
            print(f"Necessário authenticator Microsoft para continuar: {code}.")
            while True:
                body = self.find_element(by=By.TAG_NAME, value="body").text
                if "DASHBOARD" in body:
                    break
                else:
                    sleep(3)
