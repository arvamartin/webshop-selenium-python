from behave import when, then
from pages.HomePage import HomePage


@when("user selects {filter_option} option")
def user_clicks_on_filter_btn(context, filter_option):
    context.home_page = HomePage(context.driver)
    context.home_page.select_filter_option(filter_option)

@then("user sees {product} named product")
def user_sees_expected_filtered_product(context, product):
    assert context.home_page.check_expected_product(product)