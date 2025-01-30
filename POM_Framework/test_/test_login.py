from pytest import mark
from POM_Framework.Generic.lib import SeleniumWrapper
from POM_Framework.POM.Homepage import Homepage
from POM_Framework.POM.Login import Login
from POM_Framework.excel_.excel import read_headers,read_data



headers=read_headers("test_login_positive","smoke")
data=read_data("test_login_positive","smoke")

@mark.parametrize(headers,data)
def test_login(_driver,email,password):
    s = SeleniumWrapper(_driver)
    homepage = Homepage(_driver)
    homepage.click_login()
    loginpage=Login(_driver)
    loginpage.login(email,password)


