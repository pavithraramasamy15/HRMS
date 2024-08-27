from behave import given, when, then
from pageobjects.orgadmin import orgadminPageObj
from conftest import *
from selenium.webdriver.common.by import By

@given('I am on the Vignani orgadmin setupaccount')
def launchBrowser1(context):
    browser = config_parse('Browser', 'browser')
    context.driver = driversetup(browser)
    context.orgadmin_obj = orgadminPageObj(context.driver)
    context.orgadmin_obj.launchUrl1()
@when('I  enter "{Password}" and enter "{Confrimpassword}" in respective fields and click complete button')
def setupvalues(context,Password,Confrimpassword):
    context.orgadmin_obj.setupaccountvalues(Password,Confrimpassword)
# @then('the setupaccount page  should be redirected to the orgadmin dashboard')
# def verifyorgadminLoginPage(context):
#     context.orgadmin_obj.assert_manager()
@when('I navigate to the managers in the navigation Bar')
def clickmanagers(context):
    context.orgadmin_obj.click_managers()
@when('I click Add manager button')
def  verifyaddmanager(context):
    context.orgadmin_obj.click_addmanager_button()
@when('I enter"{ManagerName}",enter"{Email}" and enter"{Phonenumber}" in the respective fields')
def entermanager_details(context,ManagerName,Email,Phonenumber):
    context.orgadmin_obj.managervalues(ManagerName,Email,Phonenumber)
@then('I click save button and displays an created Successful message')
def save_button(context):
    context.orgadmin_obj.save_managers()





