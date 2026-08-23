import pytest
import time
import uuid
from automation.utils.logger import setup_logger
from automation.utils.screenshot import take_screenshot

logger = setup_logger("TestAuthFlow")

@pytest.mark.smoke
@pytest.mark.e2e
def test_register_login_logout_flow(register_page, login_page, goto_register, driver, app_url):
    """
    Test Case: E2E-01
    Steps:
    1. Navigate to Register
    2. Fill valid details with a unique username/email
    3. Submit
    4. Verify redirect to Login
    5. Fill valid credentials on Login
    6. Submit
    7. Verify Dashboard is displayed
    8. Click Logout
    9. Verify redirect to Login
    """
    # Generate unique user data to avoid duplication
    unique_id = str(uuid.uuid4())[:8]
    username = f"testuser_{unique_id}"
    email = f"test_{unique_id}@example.com"
    password = "SecurePass123"

    logger.info(f"🧪 Starting E2E test with user: {username}")

    # ----- Step 1: Register -----
    register_page.register(username, email, password)

    # ----- Step 2: Verify Registration Redirect -----
    assert register_page.is_registration_successful(), "Registration did not redirect to Login"
    logger.info("✅ Registration successful, redirected to login.")

    # ----- Step 3: Perform Login -----
    # Note: The driver is still on /login thanks to the redirect.
    # We use the login_page fixture which uses the same driver.
    login_page.login(email, password)

    # ----- Step 4: Verify Dashboard -----
    assert login_page.is_dashboard_displayed(), "Login failed, dashboard not visible"
    logger.info("✅ Login successful, dashboard is visible.")

    # Take a screenshot to prove it worked (optional but nice)
    screenshot_path = take_screenshot(driver, "E2E_Dashboard_View")
    logger.info(f"📸 Screenshot captured: {screenshot_path}")

    # ----- Step 5: Logout (via Dashboard Page) -----
    from selenium.webdriver.common.by import By
    logout_btn = (By.CSS_SELECTOR, '[data-testid="logout-btn"]')
    login_page.click(logout_btn)  # We inherit click from BasePage

    # Wait for URL to redirect to /login
    login_page.wait_for_url_contains("/login")
    
    # Verify we are on login page by checking the heading text or URL
    current_url = driver.current_url
    assert "/login" in current_url, f"Logout failed, current URL is {current_url}"
    
    logger.info("✅ Logout successful, redirected to login.")
    logger.info("🎉 End-to-End test passed successfully!")
