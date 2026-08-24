from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from automation.utils.logger import setup_logger

logger = setup_logger("DriverFactory")

def get_driver(browser_name: str = "chrome", headless: bool = False):
    """
    Returns a WebDriver instance for the specified browser.
    
    Args:
        browser_name (str): 'chrome', 'firefox', or 'edge'
        headless (bool): If True, runs browser in headless mode.
        
    Returns:
        WebDriver: Configured WebDriver instance.
    """
    browser_name = browser_name.lower()
    logger.info(f"🚀 Initializing WebDriver for: {browser_name} (headless={headless})")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-search-engine-choice-screen")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-insecure-localhost")
        options.add_argument("--disable-web-security")
        driver = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(3)
        
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(options=options)
        
    else:
        raise ValueError(f"Unsupported browser: {browser_name}. Supported: 'chrome', 'firefox', 'edge'")
    
    driver.maximize_window()
    if browser_name != "firefox":
        driver.implicitly_wait(2)
    
    logger.info(f"✅ {browser_name.capitalize()} browser initialized successfully.")
    return driver
