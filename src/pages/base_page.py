from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, base_url=None):
        self.driver = driver
        self.base_url = base_url
        self.driver.implicitly_wait(10)

    def open_root(self):
        self.driver.get(self.base_url)

    def wait_for_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_presence(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_attribute(self, locator, name, value, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).get_attribute(name) == value
        )

    def click(self, locator, timeout=20):
        self.scroll_into_view(locator)
        element = self.wait_for_clickable(locator, timeout)
        element.click()

    def type(self, locator, text, timeout=20):
        element = self.wait_for_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=5):
        element = self.wait_for_visible(locator, timeout)
        return element.text.strip()

    def is_visible(self, locator, timeout=3):
        self.wait_for_visible(locator, timeout)
        return True
           
           
    def is_element_present(self, locator, timeout=3):
        self.wait_for_presence(locator, timeout)
        return True
                
    def scroll_into_view(self, locator, timeout=5):
        element = self.wait_for_visible(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", 
            element
        )

    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)

    def wait_for_page_load(self, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
    def wait_for_url_contains(self, url_part, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: url_part in driver.current_url)

    def get_current_url(self):
        return self.driver.current_url