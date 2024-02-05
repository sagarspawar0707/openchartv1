from Framework2.pageObjects.HomePage import *
from Framework2.pageObjects.AccountRegisterPage import *
from Framework2.utility.randomString import *
import os
import time

from Framework2.utility.readproperties import getconfig
from Framework2.utility.customerLogger import *


#C:\Users\Admin\PycharmProjects\pythonSelenium\Framework1\pageObjects\HomePage.py

class Test_001_AccountReg():
    url="https://tutorialsninja.com/demo/"
    vendor = getconfig()['parameters']['Vendor']
    print(vendor)
    logger=LogGen.loggen() #for logging
    def test_account_reg(self,setup):

        self.driver=setup
        self.logger.info("*** test_001_AccountRegistration started ***")
        self.driver.get(self.url)
        self.logger.info("Launching application")
        self.driver.maximize_window()


        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.regpage=AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("White")
        self.email=random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("6565656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacypOlicy()
        self.regpage.clickContiue()
        if self.regpage.getconfimationmsg()=="Your Account Has Been Created!":
            assert True
        else:
            self.driver.save_screenshot(r"C:\Users\Admin\PycharmProjects\pythonSelenium\Framework2\Screenshots\test_account.png")
            self.driver.close()
            assert False

        self.logger.info("*** test_001_AccountRegistration ended ***")