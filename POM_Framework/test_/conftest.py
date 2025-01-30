from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver

from POM_Framework.POM.Homepage import Homepage
from POM_Framework.POM.Register import Register



# def python_addoption()
@fixture()
def _driver():
    driver=WebDriver()
    driver.get("https://demowebshop.tricentis.com")
    driver.maximize_window()
    yield driver
    driver.close()

@fixture()
def pages(_driver):

    class Pages:
        homepage = Homepage(_driver)
        registerpage = Register(_driver)
    return Pages()