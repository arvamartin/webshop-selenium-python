from utils.Browser import Browser


def before_scenario(context,driver):
    context.driver = Browser.get_driver()


def after_scenario(context,driver):
    Browser.quit_driver()