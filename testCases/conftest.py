from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "edge":
        serv_obj = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=serv_obj)
    elif browser == "chrome":
        ser_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser_obj)
    else:
        ser_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser_obj)

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_metadata(config):
    config.metadata["flight name"] = "k"
    config.metadata['Module Name'] = 'flight tickets'
    config.metadata['Tester'] = 'B.SaiKrishna'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
