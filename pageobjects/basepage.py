from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, NoSuchElementException, JavascriptException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


class ElementNotFoundException(Exception):
    pass

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def find_element(self, by, value, timeout=15):
        end_time = time.time() + timeout
        while True:
            try:
                element = self.driver.find_element(by, value)
                return element
            except Exception:
                if time.time() > end_time:
                    raise ElementNotFoundException(f"Element not found: {by}={value}")
                time.sleep(0.5)

    def click_element(self, locator):
        try:
            el = self.find_element(*locator)
            el.click()
            return True
        except TimeoutException:
            self.driver.execute_script("arguments[0].click();", el)
            return True
        except Exception:
            raise ElementNotFoundException(f"Element not clickable and JavaScript click also failed: {locator}")

    def fill_text(self, webelement, txt):
        try:
            el = self.find_element(*webelement)
            time.sleep(0.3)
            el.clear()
            time.sleep(0.3)
            el.send_keys(txt)
        except Exception:
            raise ElementNotFoundException(f"Element not found in the page so couldn't able to enter the field: {webelement}")


    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
    
    # def scroll_to_element(self, locator):
    #     try:
    #         element = self._wait.until(EC.presence_of_element_located(locator))
    #         self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", element)
    #         return element
    #     except Exception as e:
    #         print(f"Failed to scroll to element: {e}")
    #         return None
    
    def clear_fields_and_enter_value(self, element, value):
        actions = ActionChains(self.driver)
        time.sleep(1)
        actions.move_to_element(element).click().perform()
        time.sleep(1)
        length = len(element.get_attribute("value"))
        element.send_keys(Keys.BACK_SPACE * length)
        time.sleep(1)
        element.send_keys(value)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def element_screenshot(self, locator, element_name=None):
    #     if not os.path.exists("ss"):
    #         os.makedirs("ss")
    #     element = self.driver.find_element(*locator)
    #     element.screenshot(f"ss/{element_name}.png")
    

    # def wait_for_element_to_be_clickable(self, by, value):
    #     try:
    #         element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, value)))
    #         return element
    #     except TimeoutException:
    #         return None

    # def wait_for_element_to_be_visible(self, by, value):
    #     try:
    #         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))
    #         return element
    #     except TimeoutException:
    #         return None
    
    # def hover_element(driver, element):
    #     hover = ActionChains(driver).move_to_element(element)
    #     hover.perform()
    #     return element
    
    # def hover_over_element(self, locator):
    #     try:
    #         element = self.find_element(*locator)
    #         ActionChains(self.driver).move_to_element(element).perform()
    #     except Exception as e:
    #         print(f"Failed to hover over element: {e}")
    
    # def switch_to_iframe(self, locator):
    #     try:
    #         iframe = self.find_element(*locator)
    #         self.driver.switch_to.frame(iframe)
    #     except Exception as e:
    #         print(f"Failed to switch to iframe: {e}")
    
    # def select_dropdown_option_by_visible_text(self, locator, option_text):
    #     try:
    #         dropdown = Select(self.find_element(*locator))
    #         dropdown.select_by_visible_text(option_text)
    #     except Exception as e:
    #         print(f"Failed to select dropdown option by visible text: {e}")
    
    # def check_element_exists(self, locator):
    #     try:
    #         element = self.find_element(*locator)
    #         return True if element else False
    #     except Exception as e:
    #         print(f"Element does not exist: {e}")
    #         return False
    
    # def get_attribute_value(self, locator, attribute_name):
    #     try:
    #         element = self.find_element(*locator)
    #         return element.get_attribute(attribute_name)
    #     except Exception as e:
    #         print(f"Failed to get attribute value: {e}")
    #         return None
    
    # def double_click_element(self, locator):
    #     try:
    #         element = self.find_element(*locator)
    #         ActionChains(self.driver).double_click(element).perform()
    #     except Exception as e:
    #         print(f"Failed to perform double click: {e}")
    
    # def right_click_element(self, locator):
    #     try:
    #         element = self.find_element(*locator)
    #         ActionChains(self.driver).context_click(element).perform()
    #     except Exception as e:
    #         print(f"Failed to perform right click: {e}")
    
    # def drag_and_drop(self, source_locator, target_locator):
    #     try:
    #         source_element = self.find_element(*source_locator)
    #         target_element = self.find_element(*target_locator)
    #         ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
    #     except Exception as e:
    #         print(f"Failed to perform drag and drop: {e}")
    
    # def key_press(self, key):
    #     try:
    #         ActionChains(self.driver).key_down(key).key_up(key).perform()
    #     except Exception as e:
    #         print(f"Failed to perform key press action: {e}")
    
    # def click_and_hold_element(self, locator):
    #     try:
    #         element = self.find_element(*locator)
    #         ActionChains(self.driver).click_and_hold(element).perform()
    #     except Exception as e:
    #         print(f"Failed to perform click and hold action: {e}")
    
    # def release_element(self):
    #     try:
    #         ActionChains(self.driver).release().perform()
    #     except Exception as e:
    #         print(f"Failed to release element: {e}")
    
    # def select_option_by_index(self, locator, index):
    #     try:
    #         dropdown = Select(self.find_element(*locator))
    #         dropdown.select_by_index(index)
    #     except Exception as e:
    #         print(f"Failed to select option by index: {e}")
    
    # def select_option_by_visible_text(self, locator, visible_text):
    #     try:
    #         dropdown = Select(self.find_element(*locator))
    #         dropdown.select_by_visible_text(visible_text)
    #     except Exception as e:
    #         print(f"Failed to select option by visible text: {e}")
    
    # def get_all_dropdown_options(self, locator):
    #     try:
    #         dropdown = Select(self.find_element(*locator))
    #         return [option.text for option in dropdown.options]
    #     except Exception as e:
    #         print(f"Failed to get dropdown options: {e}")
    #         return []
    
    # def execute_javascript(self, script):
    #     try:
    #         self.driver.execute_script(script)
    #     except Exception as e:
    #         print(f"Failed to execute JavaScript: {e}")
    
    # def get_current_window_handle(self):
    #     try:
    #         return self.driver.current_window_handle
    #     except Exception as e:
    #         print(f"Failed to get current window handle: {e}")
    #         return None
    
    # def switch_to_window(self, window_handle):
    #     try:
    #         self.driver.switch_to.window(window_handle)
    #     except Exception as e:
    #         print(f"Failed to switch to window: {e}")
    
    # def open_new_tab(self, url):
    #     try:
    #         self.driver.execute_script(f"window.open('{url}','_blank');")
    #     except Exception as e:
    #         print(f"Failed to open new tab/window: {e}")
    
    # def get_all_window_handles(self):
    #     try:
    #         return self.driver.window_handles
    #     except Exception as e:
    #         print(f"Failed to get all window handles: {e}")
    #         return None
    
    # def close_window_by_handle(self, window_handle):
    #     try:
    #         self.driver.switch_to.window(window_handle)
    #         self.driver.close()
    #     except Exception as e:
    #         print(f"Failed to close window by handle: {e}")
    
    # def navigate_back(self):
    #     try:
    #         self.driver.back()
    #     except Exception as e:
    #         print(f"Failed to navigate back in history: {e}")

    # def navigate_forward(self):
    #     try:
    #         self.driver.forward()
    #     except Exception as e:
    #         print(f"Failed to navigate forward in history: {e}")
    
    # def refresh_page(self):
    #     try:
    #         self.driver.refresh()
    #     except Exception as e:
    #         print(f"Failed to refresh the page: {e}")
    
    #     def get_text(self, webelement):
    #     el = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
    #     self._highlight_element(el)
    #     return el.text

    # def wait_until_page_loaded(self):
    #     old_page = self.driver.find_element_by_tag_name('html')
    #     yield
    #     self._wait.until(expected_conditions.staleness_of(old_page))