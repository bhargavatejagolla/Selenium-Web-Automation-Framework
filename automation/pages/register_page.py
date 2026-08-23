from selenium.webdriver.common.by import By
from .base_page import BasePage
from automation.utils.logger import setup_logger

logger = setup_logger("RegisterPage")

class RegisterPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-testid="register-username"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="register-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="register-password"]')
    REGISTER_BTN = (By.CSS_SELECTOR, '[data-testid="register-submit"]')
    ERROR_MSG = (By.CSS_SELECTOR, '[data-testid="register-error"]')
    SUCCESS_REDIRECT = (By.CSS_SELECTOR, 'h1')  # Or we can check URL

    def register(self, username: str, email: str, password: str):
        """Perform a registration action."""
        logger.info(f"Registering user: {username} ({email})")
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.REGISTER_BTN)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MSG)

    def is_registration_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MSG)

    def is_registration_successful(self) -> bool:
        """Check if redirected to login page after successful registration."""
        self.wait_for_url_contains("/login")
        return True  # If URL contains /login, registration succeeded
