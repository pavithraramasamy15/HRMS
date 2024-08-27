from datetime import datetime
import allure, os
from behave.configuration import Configuration
from allure_behave.listener import AllureListener
import allure_commons
from functools import total_ordering


def take_screenshot(context, screenshot_name='screenshot_on_failure'):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    full_screenshot_name = f'{screenshot_name}_{current_time}.png'
    directory = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_path = os.path.join(directory, full_screenshot_name)
    
    try:
        allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        context.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
    except AttributeError as e:
        print(f"Failed to take screenshot: {e}")
        raise

def negative_scenarios_screenshot(context, screenshot_name, test_case_folder_name):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    full_screenshot_name = f'{screenshot_name}_{current_time}.png'
    directory = os.path.join(os.getcwd(), 'screenshots', test_case_folder_name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_path = os.path.join(directory, full_screenshot_name)
    allure.attach(context.driver.get_screenshot_as_png(), name=screenshot_name,
                  attachment_type=allure.attachment_type.PNG)
    context.driver.save_screenshot(screenshot_path)

@total_ordering
class ExecutionOrderMarker:
    def __init__(self, order):
        self.order = order

    def __eq__(self, other):
        return self.order == other.order

    def __lt__(self, other):
        return self.order < other.order

def before_all(context):
    behave_config = Configuration()
    listener = AllureListener(behave_config)
    allure_commons.plugin_manager.register(listener)

def before_feature(context, feature):
    context.driver = context.config.userdata.get("driver")

def get_execution_order(scenario):
    marker = scenario.tags[0] if scenario.tags else None
    if marker and marker.startswith('@order'):
        return ExecutionOrderMarker(int(marker.replace('@order', '')))
    else:
        return ExecutionOrderMarker(0)

def before_scenario(context, scenario):
    execution_order = get_execution_order(scenario)
    setattr(scenario, "execution_order", execution_order)

def after_scenario(context, scenario):
    if scenario.status == 'failed':
        take_screenshot(context)
        context.driver.quit()


def before_all(context):
    context.config.setup_logging()

def after_all(context):
    pass





