from selenium.webdriver.common.by import By
from automation.pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADING = (By.CSS_SELECTOR, '[data-testid="dashboard-heading"]')
    STATUS = (By.CSS_SELECTOR, '[data-testid="dashboard-status"]')
    LOGOUT_BTN = (By.CSS_SELECTOR, '[data-testid="logout-btn"]')

    def is_dashboard_loaded(self) -> bool:
        """Confirms the dashboard is fully loaded by checking the welcome heading."""
        return self.is_visible(self.HEADING, timeout=10)

    def get_welcome_message(self) -> str:
        return self.get_text(self.HEADING)

    def logout(self):
        self.click(self.LOGOUT_BTN)
