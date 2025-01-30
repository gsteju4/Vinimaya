from POM_Framework.Generic.lib import SeleniumWrapper
from POM_Framework.excel_.excel import read_locators
class Login:
    def __init__(self,driver):
        self.driver=driver

    loginpage=read_locators("Loginpage")

    def login(self,username,password):
        s = SeleniumWrapper(self.driver)
        # homepage = Homepage(self.driver)
        # homepage.click_login()
        s.enter_text(self.loginpage["text_email"], value=username)
        s.enter_text(self.loginpage["text_login_password"], value=password)
        s.click_element(self.loginpage["btn_login"])