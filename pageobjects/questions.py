from selenium.webdriver.common.by import By
from .basepage import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time, allure
from selenium.webdriver.support import expected_conditions as EC
from conftest import config_parse
from selenium.webdriver.common.action_chains import ActionChains
from environment import *


class QuesPageObj(BasePage):
    # login 
    email_field = (By.XPATH, "//input[@name='email']")
    password_field = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//button[@type='submit']")
    after_login_assert_element = (By.XPATH, "//title[text()='Vignani ele']")
    #question creation
    question_click=(By.XPATH,"//li[@id='Questions']/a[@href='/questions']")
    Addquestion_button=(By.XPATH,"//a[@class='flex items-center justify-center transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 h-8 rounded px-3 text-xs']")
    discipline_click=(By.XPATH,"//label[text()='Discipline']/following-sibling::button")
    discipline_select=(By.XPATH,"//span[text()='Mechanical']")
    subject_click=(By.XPATH,"//label[text()='Subject']/following-sibling::button")
    subject_select=(By.XPATH,"//span[text()='Metrology']")
    # types_select=(By.XPATH,"//input[@value='SEAT']")
    difficulty_select=(By.XPATH,"//button[@value='INTERMEDIATE']")
    question_enter=(By.XPATH,"//div[@class='cm-content cm-lineWrapping']")
    optionA_enter=(By.XPATH,"//textarea[@name='optionA']")
    optionB_enter=(By.XPATH,"//textarea[@name='optionB']")
    optionC_enter=(By.XPATH,"//textarea[@name='optionC']")
    optionD_enter=(By.XPATH,"//textarea[@name='optionD']")
    answer_click=(By.XPATH,"//label[text()='Answer']/following-sibling::button")
    answer_select=(By.XPATH,"//span[text()='A']")
    weightage_click=(By.XPATH,"//label[text()='Weightage']/following-sibling::button")
    weightage_select=(By.XPATH,"//div[@role='option']/span[text()='10']")
    create_click=(By.XPATH,"//button[text()='Create']")
    search_ques=(By.XPATH,"//input[@placeholder='Search Question...']")
    assert_ques=(By.XPATH,"//div[text()='What is the material of the bench center’s base?']")
    # Edit Questions
    search_box=(By.XPATH,"//input[@placeholder='Search Question...']")
    actions_click=(By.XPATH,"//div[@class='flex flex-row justify-center gap-2']")
    edit_click=(By.XPATH,"//span[@class='flex items-center text-primary hover:text-primary']")
    edit_difficulty=(By.XPATH,"//button[@value='INTERMEDIATE']")
    update_click=(By.XPATH,"//button[@type='submit']")





    def __init__(self, driver):
        super().__init__(driver)
    def launchUrl(self):
        login_url = config_parse('vignani_url', 'base_url')
        self.driver.get(login_url)
    def enterCredentials1(self, email, password):
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

    def assertLogin1(self):
        assert self.find_element(*self.after_login_assert_element)

    def click_question(self):
        self.click_element(self.question_click)
    def click_addques_button(self):
        self.click_element(self.Addquestion_button)
    def enterdetails1(self,Questions,optionA,optionB,optionC,optionD):
        if Questions =="<Questions>":
            Questions =config_parse('Add_questions','Questions')
        if optionA == "<optionA>":
            optionA = config_parse('Add_questions','optionA')
        if optionB == "<optionB>":
            optionB = config_parse('Add_questions','optionB')
        if optionC == "<optionC>":
            optionC = config_parse('Add_questions','optionC')
        if optionD == "<optionD>":
            optionD = config_parse('Add_questions','optionD')
        
        self.click_element(self.discipline_click)
        self.click_element(self.discipline_select)
        self.click_element(self.subject_click)
        self.click_element(self.subject_select)
        # self.click_element(self.types_select)
        self.click_element(self.difficulty_select)
        self.fill_text(self.question_enter,Questions)
        self.fill_text(self.optionA_enter,optionA)
        self.fill_text(self.optionB_enter,optionB)
        self.fill_text(self.optionC_enter,optionC)
        self.fill_text(self.optionD_enter,optionD)
        self.click_element(self.answer_click)
        self.click_element(self.answer_select)
        self.click_element(self.weightage_click)
        self.click_element(self.weightage_select)
    def create_ques(self):
        self.click_element(self.create_click)
        time.sleep(8)

    def assertques(self,question):
        if question =="<question>":
            question=config_parse('search_ques','question')
            self.fill_text(self.search_ques,question)
            assert self.find_element(*self.assert_ques)
            time.sleep(5)
    # Edit_ques
    def editquesfill(self,ques):
        if ques=="<ques>":
            ques=config_parse('search_box','ques')
            self.fill_text(self.search_box,ques)
    
    def actionfield_click(self):
        self.click_element(self.actions_click)

    def editoption_click(self):
        self.click_element(self.edit_click)
        self.click_element(self.edit_difficulty)

    def update_button(self):
        self.click_element(self.update_click)
        time.sleep(7)
        

        
    
        
        

