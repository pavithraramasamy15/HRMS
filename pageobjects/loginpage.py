from selenium.webdriver.common.by import By
from .basepage import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time, allure
from selenium.webdriver.support import expected_conditions as EC
from conftest import config_parse
from selenium.webdriver.common.action_chains import ActionChains
from environment import *



class LoginPageObj(BasePage):
    email_field = (By.XPATH, "//input[@name='email']")
    password_field = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//button[@type='submit']")
    login_assert_element_1 = (By.XPATH, "//h3[text()='Welcome']")
    login_assert_element_2 = (By.XPATH, "//p[text()='Please enter your credentials to sign in.']")
    after_login_assert_element = (By.XPATH, "//title[text()='Vignani ele']")
    logout_button = (By.XPATH, "//button[text()='Logout']")
    # invalid_credentials_error = (By.XPATH, "//h5[text()='Invalid credentials']")
    
    
    org_click=(By.XPATH,"//li[@id='Organization']/a[@href='/org']")
    addorg_button=(By.XPATH,"//a[@class='flex items-center justify-center transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-8 rounded px-3 text-xs']")
    org_name=(By.XPATH,"//input[@name='organization_name']")
    Domain_click=(By.XPATH,"//input[@placeholder='Select a Domain']")
    select_domain=(By.XPATH,"//div[@data-value='Power']")
    org_address=(By.XPATH,"//textarea[@name='organization_address']")
    email_address=(By.XPATH,"//input[@name='organization_email']")
    save_button=(By.XPATH,"//button[@type='submit']")
    
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def launchUrl(self):
        login_url = config_parse('vignani_url', 'base_url')
        self.driver.get(login_url)
    
    def verifyLoginPage(self):
        assert self.find_element(*self.login_assert_element_1) and self.find_element(*self.login_assert_element_2)
    
    def enterCredentials(self, email, password):
        if email == "<email>":
            email = config_parse('sign_in_cred', 'email')
        elif email == "EMPTY":
            email = ""                 # Treat empty email as empty string
        if password == "<password>":
            password = config_parse('sign_in_cred', 'password')
        elif password == "EMPTY":
            password = ""              # Treat empty password as empty string
            
        self.fill_text(self.email_field, email)
        self.fill_text(self.password_field, password)
        self.click_element(self.submit_button)
        time.sleep(10)

    
    def assertLogin(self):
        assert self.find_element(*self.after_login_assert_element)
    
    
    
    # def verifyInvalidCredentials(self):
    #     assert self.find_element(*self.invalid_credentials_error)

    

    def click_org(self):
        self.click_element(self.org_click)

    def click_addorg_button(self):
        self.click_element(self.addorg_button)

    def enterdetails(self,Organization_Name,Organization_Address,Email_Address):
        if Organization_Name =="<Organization_Name>":
            Organization_Name =config_parse('Add_org','Organization_Name')
        
        if Organization_Address == "<Organization_Address>":
            Organization_Address = config_parse('Add_org','Organization_Address')
        if Email_Address == "<Email_Address>":
            Email_Address=config_parse('Add_org','Email_Address')
        
        self.fill_text(self.org_name,Organization_Name )
        self.click_element(self.Domain_click)
        self.click_element(self.select_domain)
        self.fill_text(self.org_address,Organization_Address)
        self.fill_text(self.email_address,Email_Address)

    def save(self):
        self.click_element(self.save_button)
        time.sleep(5)

    def clickLogout(self):
        self.click_element(self.logout_button)

    

    