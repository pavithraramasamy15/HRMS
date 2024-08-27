from selenium.webdriver.common.by import By
from .basepage import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time, allure
from selenium.webdriver.support import expected_conditions as EC
from conftest import config_parse
from selenium.webdriver.common.action_chains import ActionChains
from environment import *
class orgadminPageObj(BasePage):
    # set up account
    # name_field=(By.XPATH,"//input[@value='kovanlabs']")
    password_field=(By.XPATH,"//input[@name='password']")
    confrimpassword_field=(By.XPATH,"//input[@name='confirm_password']")
    complete_click=(By.XPATH,"//button[@type='submit']")
    # assermanager=(By.XPATH,"//h3[@class='text-xl font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 flex items-center justify-between']")
    # manager add
    manager_click=(By.XPATH,"//li[@id='Managers']/a[@href='/manager']")
    addmanager_button=(By.XPATH,"//a[@class='flex items-center justify-center transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-8 rounded px-3 text-xs']")
    manager_name=(By.XPATH,"//input[@name='name']")
    manager_email=(By.XPATH,"//input[@name='email']")
    manager_phonenumber=(By.XPATH,"//input[@name='phone_number']")
    manager_save=(By.XPATH,"//button[@type='submit']")
    def __init__(self, driver):
        super().__init__(driver)
    def launchUrl1(self):
        login1_url = config_parse('orgadmin_url', 'setup_url')
        self.driver.get(login1_url)
    def setupaccountvalues(self,Password,Confrimpassword):
        # if OrgName == "<OrgName>":
        #     OrgName = config_parse('setup_account_values', 'name')
        if Password== "<Password>":
            Password =config_parse('setup_account_values','password')
        if Confrimpassword == "<Confrimpassword>" :
            Confrimpassword =config_parse('setup_account_values','confrimpassword')
        
        # self.fill_text(self.name_field,OrgName)
        self.fill_text(self.password_field,Password)
        self.fill_text(self.confrimpassword_field,Confrimpassword)
        self.click_element(self.complete_click)
        time.sleep(7)

    # def assert_manager(self):
    #     assert self.find_element(*self.assermanager)

    def click_managers(self):
        self.click_element(self.manager_click)
    def click_addmanager_button(self):
        self.click_element(self.addmanager_button)
    def managervalues(self,ManagerName,Email,Phonenumber):
        if ManagerName ==  "<ManagerName>":
            ManagerName =config_parse('Add_managers','managerName')
        if Email ==  "<Email>":
            Email =config_parse('Add_managers','managerEmail')
        if Phonenumber ==  "<Phonenumber>":
           Phonenumber =config_parse('Add_managers','manger_contact')
        
        self.fill_text(self.manager_name,ManagerName)
        self.fill_text(self.manager_email,Email)
        self.fill_text(self.manager_phonenumber,Phonenumber)
    
    def save_managers(self):
        self.click_element(self.manager_save)
        time.sleep(5)


    

        
        



