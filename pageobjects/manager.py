from selenium.webdriver.common.by import By
from .basepage import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time, allure
from selenium.webdriver.support import expected_conditions as EC
from conftest import config_parse
from selenium.webdriver.common.action_chains import ActionChains
from environment import *

class managerPageObj(BasePage):
    # setupaccount
    password_field=(By.XPATH,"//input[@name='password']")
    confrimpassword_field=(By.XPATH,"//input[@name='confirm_password']")
    complete_button=(By.XPATH,"//button[@type='submit']")
    # add candidate
    candidate_click=(By.XPATH,"//li[@id='Candidates']/a[@href='/candidate']")
    Addcandidate_click=(By.XPATH,"//a[@class='flex items-center justify-center transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-8 rounded px-3 text-xs']")
    disciplineclick=(By.XPATH,"//label[text()='Discipline']/following-sibling::button")
    discipline_values=(By.XPATH,"//span[text()='Electrical']")
    candidatename_field=(By.XPATH,"//input[@name='name']")
    email_field=(By.XPATH,"//input[@name='email']")
    contactnumber_field=(By.XPATH,"//input[@name='number']")
    jobrolefield_click=(By.XPATH,"//label[text()='Job Role']/following-sibling::button")
    jobrole_values=(By.XPATH,"//span[text()='Quality Engineers']")
    groupid_field=(By.XPATH,"//label[text()='Group Id']/following-sibling::button")
    groupid_values=(By.XPATH,"//span[text()='JOB_ID_1']")
    save_field=(By.XPATH,"//button[@type='submit']")
    # assign assignments
    assign_click=(By.XPATH,"//li[@id='Assign']/a[@href='/manager/assignAssessments']")
    viewuser_click=(By.XPATH,"//button[@id='user-display-button']")
    close_user=(By.XPATH,"//button[@class='absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground']")
    seat_packages_click=(By.XPATH,"//button[@id='seat-checkbox-clyj176rg00011pj4az263rdf']")
    # view_cart_click=(By.XPATH,"//button[@id='view-cart-button']")
    # viewcart_close=(By.XPATH,"//button[@class='absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-secondary']")
    save_packages=(By.XPATH,"//button[text()='Save']")
    assign_button_click=(By.XPATH,"//button[text()='Assign']")



    def __init__(self, driver):
        super().__init__(driver)
    def launchUrl2(self):
        login2_url = config_parse('manager_url', 'setupaccount_url')
        self.driver.get(login2_url)
    def setupaccountvalues1(self,Password,Confrimpassword):
        if Password== "<Password>":
            Password =config_parse('setaccount_manager','password1')
        if Confrimpassword == "<Confrimpassword>" :
            Confrimpassword =config_parse('setaccount_manager','confrimpassword1')
        
        self.fill_text(self.password_field,Password)
        self.fill_text(self.confrimpassword_field,Confrimpassword)
        self.click_element(self.complete_button)
        time.sleep(7)
    
    def click_candidate(self):
        self.click_element(self.candidate_click)
    def click_addcandidate_button(self):
        self.click_element(self.Addcandidate_click)
    def candidatevalues(self,CandidateName,Email,Contactnumber):
        if CandidateName ==  "<CandidateName>":
            CandidateName =config_parse('Add_candidate','CandidateName')
        if Email ==  "<Email>":
            Email =config_parse('Add_candidate','Email')
        if Contactnumber ==  "<Contactnumber>":
           Contactnumber =config_parse('Add_candidate','Contactnumber')
        
        self.click_element(self.disciplineclick)
        self.click_element(self.discipline_values)
        self.fill_text(self.candidatename_field,CandidateName)
        self.fill_text(self.email_field,Email)
        self.fill_text(self.contactnumber_field,Contactnumber)
        self.click_element(self.jobrolefield_click)
        self.click_element(self.jobrole_values)
        self.click_element(self.groupid_field)
        self.click_element(self.groupid_values)

    def save_candidate(self):
        self.click_element(self.save_field)
        time.sleep(8)
    
    def click_assign(self):
        self.click_element(self.assign_click)
    def add_assessments(self):
        self.click_element(self.viewuser_click)
        self.click_element(self.close_user)
        self.click_element(self.seat_packages_click)
        # self.click_element(self.view_cart_click)
        # self.click_element(self.viewcart_close)
        
    def save_assign(self):
        self.click_element(self.save_packages)  
        self.click_element(self.assign_button_click)
        time.sleep(7)
        







