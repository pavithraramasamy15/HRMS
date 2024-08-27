from selenium import webdriver
import pytest, configparser, os, time, json
from datetime import datetime
import allure

def config_parse(section, key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get(section, key)


@pytest.mark.usefixtures()
def driversetup(browser):
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Firefox(options=options)
    elif browser.lower() == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
        
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driversetup')
        if driver:
            time.sleep(1)
            take_screenshot(driver)

def take_screenshot(driver, screenshot_name='screenshot_on_failure'):
    current_time = datetime.now().strftime("%Y--%m--%d_%H-%M-%S")
    full_screenshot_name = f'{screenshot_name}_{current_time}.png'
    directory = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_path = os.path.join(directory, full_screenshot_name)
    allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
                attachment_type=allure.attachment_type.PNG)
    driver.save_screenshot(screenshot_path)