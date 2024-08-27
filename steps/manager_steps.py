from behave import given, when, then
from pageobjects.manager import managerPageObj
from conftest import *
from selenium.webdriver.common.by import By

@given('I am on the Vignani Manager setupaccount')
def launchBrowser2(context):
    browser = config_parse('Browser', 'browser')
    context.driver = driversetup(browser)
    context.manager_obj =managerPageObj(context.driver)
    context.manager_obj.launchUrl2()

@when('I enter values in "{Password}" and enter values in "{Confrimpassword}" in respective fields and then click complete button')
def setupvalues_candidate(context,Password,Confrimpassword):
    context.manager_obj.setupaccountvalues1(Password,Confrimpassword)


@when('I navigate to the candidates in the navigation Bar')
def clickcandidates(context):
    context.manager_obj.click_candidate()

@when('I click Add candidate  button')
def  verifyaddcandidate(context):
    context.manager_obj.click_addcandidate_button()

@when('I select Discipline from dropdown values,enter "{CandidateName}",enter "{Email}",enter "{Contactnumber}",select jobid from dropdownvalues,and select groupid from dropdown values')
def entercandidate_details(context,CandidateName,Email,Contactnumber):
    context.manager_obj.candidatevalues(CandidateName,Email,Contactnumber)

@then('I clicking the save button and displays an created candidate Successful message')
def savecandidate_button(context):
    context.manager_obj.save_candidate()

@when('I click the assign in the navigation Bar')
def clickassign(context):
    context.manager_obj.click_assign()
@then('I select jobid in dropdown values,view users under jobid,select packages,view carts')
def addassessments(context):
    context.manager_obj.add_assessments()

@then('I click save button and displays an success message  assign packages to the candidate')
def savepackages(context):
    context.manager_obj.save_assign()
    



