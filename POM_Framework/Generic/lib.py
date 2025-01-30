from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def _wait(fun):
    def wrapper(*args,**kwargs):
        instance,locator=args
        w=WebDriverWait(instance.driver,10)
        v=visibility_of_element_located(locator)
        w.until(v)
        return fun(*args,**kwargs)
    return wrapper

def wait_cls(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key!="__init__":
            setattr(cls,key,_wait(value))

    return cls



@wait_cls
class SeleniumWrapper:

    def __init__(self,driver):
        self.driver=driver

    def click_element(self,locator):
        loc_type,loc_value=locator
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,*,value):
        loc_type,loc_value=locator
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def select_item(self,locator,*,item):
        loc_type,loc_value=locator
        element=self.find_element(*locator)
        select=Select(element)
        select.select_by_visible_text(item)

    def mouse_act(self,locator):
        loctype,loc_value=locator
        act_obj=ActionChains(self.driver)
        element=self.find_element(*locator)
        act_obj.move_to_element(element).perform()

    def page_downaction(self):
        act_obj = ActionChains(self.driver)
        act_obj.send_keys(Keys.PAGE_DOWN).perform()

    def page_upaction(self):
        act_obj = ActionChains(self.driver)
        act_obj.send_keys(Keys.PAGE_UP).perform()




