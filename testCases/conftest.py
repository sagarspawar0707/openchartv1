from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option("detach", True)
        driver=webdriver.Edge(options=opts)
        print("launching Edge browser")
    elif browser  ==  'fireFox':
        driver=webdriver.Firefox()
        print("launching fireFox...........")
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        #chrome_options.add_argument('--ignore-certificate-errors')
        #chrome_options.add_argument('--disable-web-security')
        #chrome_options.add_argument('--allow-running-insecure-content')
        #chrome_options.add_argument('--ignore-ssl-errors=yes')
        #chrome_options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
