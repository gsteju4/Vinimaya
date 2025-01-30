from POM_Framework.Generic.lib import SeleniumWrapper
from POM_Framework.excel_.excel import read_locators
class Category:
    def __init__(self,driver):
        self.driver=driver

    categorypage = read_locators("Categories")

    def click_books(self,category):
        s = SeleniumWrapper(self.driver)
        # homepage = Homepage(self.driver)
        # homepage.click_login()
        s.mouse_act(self.categorypage["link_Books"].perform())




        s.mouse_act(s.Categories["link_Books"])
