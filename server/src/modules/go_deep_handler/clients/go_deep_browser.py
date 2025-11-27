from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from os import getenv
from dotenv import load_dotenv
from time import sleep

class GoDeepBrowser:
    
    def _instance_chrome(self, headless: bool) -> None:
        options = Options()
        options.add_argument(argument="--disable-logging")
        options.add_argument(argument="--log-level=3")
        options.add_argument(argument="--silent")
        options.add_argument(argument="--v=0")
        options.add_experimental_option(name="useAutomationExtension", value=False)
        options.add_experimental_option(name="excludeSwitches", value=["enable-automation", "enable-logging"])
        if headless:
            options.add_argument(argument="--headless=new")
        else:
            options.add_experimental_option(name="detach", value=True)
        self.driver = Chrome(options=options)
    
    def _login(self) -> None:
        load_dotenv()
        self.driver.get(f"https://www.revendedorpositivo.com.br/admin/")
        user = self.driver.find_element(by=By.ID, value="username")
        password = self.driver.find_element(by=By.ID, value="password")
        login_button = self.driver.find_element(by=By.XPATH, value="//div[@id='action-login']/div[@class='col-md-12 pad-right0 pad-left0']/button[@class=' col-md-12 btn btn-primary button-login-home pad-bottom10']")
        user_env = getenv("GODEEP_EMAIL")
        password_env = getenv("GODEEP_PASSWORD")
        if user_env and password_env:
            user.send_keys(user_env)
            password.send_keys(password_env)
        login_button.click()
        sleep(1)
        body = self.driver.find_element(by=By.TAG_NAME, value="body").text
        if any(login_string in body for login_string in ["Because you're accessing sensitive info, you need to verify your password.", "Sign in", "Pick an account", "Entrar"]):
            print("Necessário logar conta Microsoft.")
            while True:
                body = self.driver.find_element(by=By.TAG_NAME, value="body").text
                if "DASHBOARD" in body:
                    break
                else:
                    sleep(3)
        if "Approve sign in request" in body:
            sleep(1)
            code = self.driver.find_element(by=By.ID, value="idRichContext_DisplaySign").text
            print(f"Necessário authenticator Microsoft para continuar: {code}.")
            while True:
                body = self.driver.find_element(by=By.TAG_NAME, value="body").text
                if "DASHBOARD" in body:
                    break
                else:
                    sleep(3)
    
    def init(self, headless: bool) -> None:
        try:
            self._instance_chrome(headless=headless)
            self._login()
        except Exception as error:
            raise Exception(f"Error in (GoDeepBrowser) component in (init) method: {error}.")
    
    def quit(self) -> None:
        try:
            self.driver.quit()
        except Exception as error:
            raise Exception(f"Error in (GoDeepBrowser) component in (quit) method: {error}.")
