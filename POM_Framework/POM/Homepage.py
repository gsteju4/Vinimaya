from POM_Framework.Generic.lib import SeleniumWrapper
from POM_Framework.excel_.excel import read_locators

class Homepage:
    def __init__(self,driver):
        self.driver=driver

    homepage_= read_locators("Homepage")


    def click_register(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self.homepage_["btn_register"])

    def click_login(self):
        s=SeleniumWrapper(self.driver)
        s.click_element(self.homepage_["btn_login"])






