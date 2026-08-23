from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from automation.utils.logger import setup_logger

logger = setup_logger("BasePage")

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, ignored_exceptions=[StaleElementReferenceException])

    def click(self, locator):
        logger.info(f"🖱️ Clicking on element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        display_text = "******" if "password" in str(locator).lower() else text
        logger.info(f"⌨️ Entering text '{display_text}' into: {locator}")
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        text = self.wait.until(EC.visibility_of_element_located(locator)).text
        logger.info(f"Retrieved text: '{text}' from: {locator}")
        return text

    def is_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, partial_url, timeout=5):
        logger.info(f"Waiting for URL to contain: {partial_url}")
        WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))
