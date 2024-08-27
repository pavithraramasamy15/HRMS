from behave import given, when, then
from pageobjects.questions import QuesPageObj
from conftest import *
from selenium.webdriver.common.by import By
@given('I am on the Vignani page')
def launchBrowser(context):
    browser = config_parse('Browser', 'browser')
    context.driver = driversetup(browser)
    context.ques_obj = QuesPageObj(context.driver)
    context.ques_obj.launchUrl()

@when('I input "{email}" and "{password}"  and press the submit  button')
def enterCred1(context, email, password):
    context.ques_obj.enterCredentials1(email, password)

@then('I should be redirected to the Admin dashboard and the page title should be VignaniELE')
def verifyLoginPage1(context):
    context.ques_obj.assertLogin1()

@when('I navigate to the Questions in the navigation Bar')
def clickques(context):
    context.ques_obj.click_question()

@when('I click Add Questions button')
def click_addques_button(context):
    context.ques_obj.click_addques_button()

@when('I select Discipline in dropdown, select subject in dropdown,select type ,select difficulty,enter "{Questions}" in textbox,enter "{optionA}",enter "{optionB}",enter "{optionC}",enter "{optionD}",select Answer in dropdown,select Weightage in dropdown')
def entervalues1(context,Questions,optionA,optionB,optionC,optionD):
    context.ques_obj.enterdetails1(Questions,optionA,optionB,optionC,optionD)

@when('I click create button')
def createbutton(context):
    context.ques_obj.create_ques()

@then('the question created successfully with the message and "{question}" should be in questionslist')
def verifyquescreation(context,question):
    context.ques_obj.assertques(question)

# edit steps
@when('I select the question to changes  in  questions "{ques}"')
def quesedit(context,ques):
    context.ques_obj.editquesfill(ques)
@when('I click the Actions icon to edit the question')
def clickactions(context):
    context.ques_obj.actionfield_click()

@when('I click the edit option and edit the changes in questions')
def clickedit_ques(context):
    context.ques_obj.editoption_click()

@then('I click the Update button and see the  successfully updated questions pop up message')
def clickupdate_button(context):
    context.ques_obj.update_button()



