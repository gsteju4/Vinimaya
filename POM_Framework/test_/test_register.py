from pytest import mark
from POM_Framework.excel_.excel import read_headers,read_data



headers=read_headers("test_registration","smoke")
data=read_data("test_registration","smoke")

@mark.parametrize(headers,data)
def test_register(pages,gender,fname,lname,email,password,confirmpassword):
    # s=SeleniumWrapper(_driver)


    pages.homepage.click_register()

    pages.registerpage.register(gender,fname,lname,email,password,confirmpassword)


