from POM_Framework.Generic.lib import SeleniumWrapper
from POM_Framework.POM.Homepage import Homepage
from POM_Framework.excel_.excel import read_locators
class Register:
    def __init__(self,driver):
        self.driver=driver

    registerpage=read_locators("Registerpage")

    def register(self,gender,fname,lname,email,password,confirmpassword):
        s = SeleniumWrapper(self.driver)
        homepage = Homepage(self.driver)
        homepage.click_register()
        if gender.upper()=="MALE":
            s.click_element(self.registerpage["rdo_male"])
        elif gender.upper()=="FEMALE":
            s.click_element(self.registerpage["rdo_female"])

        s.enter_text(self.registerpage["text_firstname"],value=fname)
        s.enter_text(self.registerpage["text_lastname"],value=lname)
        s.enter_text(self.registerpage["text_email"], value=email)
        s.enter_text(self.registerpage["text_password"],value=password)
        s.enter_text(self.registerpage["text_confirm"],value=confirmpassword)
        s.click_element(self.registerpage["btn__reg_success"])
