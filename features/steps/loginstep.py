from behave import given,when,then
from pages.LoginPage import LoginPage
from utils.ConfigReader import ConfigReader


@given("user is already on the login page")
def user_is_on_the_login_page(context):
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)


@when("user enters username {username} into username input")
def user_enters_username(context, username):
    context.login_page.enter_username(username)


@when("user enters password {password} into password input")
def user_enters_password(context, password):
    context.login_page.enter_password(password)


@when('user clicks on login button')
def user_click_on_login_btn(context):
    context.login_page.click_login_btn()


@then("user is on the home page")
def user_is_on_the_home_page(context):
    expected_url = ConfigReader.get_property("Basic info", "home_page_url")
    actual_url = context.driver.current_url
    assert expected_url == actual_url

@then("user remained on the login page")
def user_remained_on_the_login_page(context):
    expected_url = ConfigReader.get_property("Basic info", "login_url")
    actual_url = context.driver.current_url
    assert expected_url == actual_url