from behave import when, then

from pages.HomePage import HomePage


@when("user clicks on the menu button")
def user_clicks_on_menu_btn(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_menu_btn()

@when("user clicks on the logout button")
def user_clicks_on_logout_btn(context):
    context.home_page.click_on_logout_btn()

@then("user is redirected to the login page")
def user_is_redirected_to_login_page(context):
    print("none")
