from behave import given, when, then
from pageobjects.loginpage import LoginPageObj
from conftest import *
from selenium.webdriver.common.by import By


@given('I am on the Vignani login page')
def launchBrowser(context):
    browser = config_parse('Browser', 'browser')
    context.driver = driversetup(browser)
    context.login_obj = LoginPageObj(context.driver)
    context.login_obj.launchUrl()

@then("I should able to see the login page elements for login page verification")
def verifyLaunchPage(context):
    context.login_obj.verifyLoginPage()

@when('I enter "{email}" and "{password}" in the respective fields and clicked on Signin button')
def enterCred(context, email, password):
    context.login_obj.enterCredentials(email, password)

@then("the login page should be redirected to the Trainee dashboard and I should see the title for the login page verification")
def verifyLoginPage(context):
    context.login_obj.assertLogin()



# @then("It should be redirected to the login page and I should see the Welcome title")
# def verifyLogout(context):
#     context.login_obj.verifyLoginPage()

# @then("The login page should display error message as invalid credentials")
# def assertInvalidCredentials(context):
#     context.login_obj.verifyInvalidCredentials()

@when("I navigate to the organization in the navigation Bar")
def clickorg(context):
    context.login_obj.click_org()

@when("I click Add organization button")
def click_addorg_button(context):
    context.login_obj.click_addorg_button()

@when('I Enter "{Organization_Name}", Select Domain in Dropdown values, Enter "{Organization_Address}", Enter "{Email_Address}"')
def entervalues(context,Organization_Name,Organization_Address,Email_Address):
    context.login_obj.enterdetails(Organization_Name,Organization_Address,Email_Address)

@then("I click the save button")
def savebutton(context):
    context.login_obj.save()
@then("I click logout button")
def performLogout(context):
    context.login_obj.clickLogout()