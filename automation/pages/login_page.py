from selenium.webdriver.common.by import By
from .base_page import BasePage
from automation.utils.logger import setup_logger

logger = setup_logger("LoginPage")

class LoginPage(BasePage):
    # Locators - using data-testid from our Next.js app
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="login-email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-testid="login-submit"]')
    ERROR_MSG = (By.CSS_SELECTOR, '[data-testid="login-error"]')
    DASHBOARD_HEADING = (By.CSS_SELECTOR, '[data-testid="dashboard-heading"]')

    def login(self, email: str, password: str):
        """Perform a login action."""
        logger.info(f"Logging in with email: {email}")
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self) -> str:
        """Retrieve the error message displayed on login failure."""
        return self.get_text(self.ERROR_MSG)

    def is_login_error_displayed(self) -> bool:
        """Check if error message is visible."""
        return self.is_visible(self.ERROR_MSG)

    def is_dashboard_displayed(self) -> bool:
        """Check if dashboard heading is visible (indicates successful login)."""
        # Wait for URL to change to dashboard as well for robustness
        self.wait_for_url_contains("/dashboard")
        return self.is_visible(self.DASHBOARD_HEADING)
