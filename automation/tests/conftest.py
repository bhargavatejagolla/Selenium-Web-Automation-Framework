import pytest
import requests
import time
from selenium import webdriver
from automation.utils.driver_factory import get_driver
from automation.pages.login_page import LoginPage
from automation.pages.register_page import RegisterPage
from automation.utils.logger import setup_logger
from automation.utils.data_generator import generate_real_user
from automation.utils.screenshot import take_screenshot

logger = setup_logger("PytestSetup")

# ---------- HTML Report Screenshot Hook ----------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            logger.info(f"📸 Screenshot captured for failed test: {screenshot_path}")
            try:
                from pytest_html import extras
                html_screenshot = extras.image(screenshot_path, mime_type='image/png')
                if hasattr(rep, 'extra'):
                    rep.extra.append(html_screenshot)
                else:
                    rep.extra = [html_screenshot]
            except ImportError:
                pass

# ---------- Rich Console Dashboard Hook ----------
def pytest_sessionfinish(session, exitstatus):
    try:
        from rich.console import Console
        from rich.table import Table
        from rich import box
        
        console = Console()
        tests_collected = session.testscollected
        if tests_collected == 0:
            return

        failed = getattr(session, 'testsfailed', 0)
        skipped = 0 
        passed = tests_collected - failed - skipped
        pass_rate = (passed / tests_collected * 100) if tests_collected > 0 else 0
        
        console.print("\n")
        console.rule("[bold cyan]🔍 TEST EXECUTION SUMMARY[/bold cyan]")
        console.print("\n")

        table = Table(title="Automation Test Report", box=box.ROUNDED, style="bright_white")
        table.add_column("Status", style="cyan", no_wrap=True)
        table.add_column("Count", justify="right", style="bold")
        table.add_column("Percentage", justify="right")

        table.add_row("✅ Passed", str(passed), f"{pass_rate:.1f}%")
        table.add_row("❌ Failed", str(failed), f"{(failed/tests_collected*100) if tests_collected>0 else 0:.1f}%")
        table.add_row("📦 Total", str(tests_collected), "100%")

        console.print(table)
        
        if failed > 0:
            console.print("[bold red]❌ Failed Tests:[/bold red]")
        else:
            console.print("[bold green]🎉 All tests passed! Great job![/bold green]")
        
        console.print("\n")
        console.rule("[bold cyan]End of Report[/bold cyan]")
        console.print("\n")
    except ImportError:
        pass

# ---------- Report Metadata ----------
def pytest_configure(config):
    """Add custom metadata to the HTML report."""
    if hasattr(config, '_metadata'):
        config._metadata['Browser'] = config.getoption("--browser")
        config._metadata['Headless'] = str(config.getoption("--headless"))
        config._metadata['Application URL'] = config.getoption("--app-url")

# ---------- Command Line Options ----------
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on: chrome, firefox, edge")
    parser.addoption("--headless", action="store_true", default=False, help="Run browser in headless mode")
    parser.addoption("--app-url", action="store", default="http://localhost:3000", help="Base URL of the application")

@pytest.fixture(scope="session")
def app_url(request):
    return request.config.getoption("--app-url")

@pytest.fixture(scope="session", autouse=True)
def check_app_health(app_url):
    logger.info(f"🔍 Checking application health at: {app_url}")
    try:
        response = requests.get(app_url, timeout=5)
        if response.status_code == 200:
            logger.info("✅ Application is reachable and healthy.")
    except Exception as e:
        pytest.fail(f"🚨 Application is not running at {app_url}. Tests aborted.")

@pytest.fixture(scope="session")
def real_test_user(app_url):
    user_data = generate_real_user()
    logger.info(f"🛠️ Creating Real Test User in DB: {user_data['email']}")
    try:
        response = requests.post(f"{app_url}/api/auth/register", json=user_data)
        if response.status_code == 201:
            logger.info("✅ Real test user created successfully.")
            return user_data
        else:
            pytest.fail(f"Failed to create real test user. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        pytest.fail(f"Error creating real test user: {e}")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    driver = get_driver(browser, headless=headless)
    yield driver
    
    logger.info("🛑 Closing browser")
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)

@pytest.fixture
def goto_login(driver, app_url):
    driver.get(f"{app_url}/login")
    time.sleep(0.5)
    return driver

@pytest.fixture
def goto_register(driver, app_url):
    driver.get(f"{app_url}/register")
    time.sleep(0.5)
    return driver
