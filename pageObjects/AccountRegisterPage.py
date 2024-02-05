from selenium import webdriver
from selenium.webdriver.common.by import By
#from Framework2.utility.customerLogger import LogGen



class AccountRegistrationPage():
      driver=webdriver.Chrome()
      txt_firstname_name="firstname"
      txt_lastname_name="lastname"
      txt_email_name="email"
      txt_telephone_name="telephone"
      txt_password_name="password"
      txt_confpassword_name="confirm"
      chk_policy_xpath="//input[@name='agree']"
      btn_cont_xpath="//input[@value='Continue']"
      txt_msg_conf_xpath="//h1[text()='Your Account Has Been Created!']"

      def __init__(self,driver):
           self.driver=driver


      def setFirstName(self,fname):
          self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

      def setLastName(self,lname):
          self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)


      def setEmail(self,email):
          self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)


      def setTelephone(self,Tel):
          self.driver.find_element(By.NAME,self.txt_telephone_name).send_keys(Tel)


      def setPassword(self,pwd):
          self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

      def setConfirmPassword(self,cpwd):
          self.driver.find_element(By.NAME,self.txt_confpassword_name).send_keys(cpwd)

      def setPrivacypOlicy(self):
          self.driver.find_element(By.XPATH, self.chk_policy_xpath).click()

      def clickContiue(self):
          self.driver.find_element(By.XPATH, self.btn_cont_xpath).click()


      def getconfimationmsg(self):
          try:
              return self.driver.find_element(By.XPATH,self.txt_msg_conf_xpath).text
          except:
              None