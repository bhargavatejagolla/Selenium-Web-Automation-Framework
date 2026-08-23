import pytest
from automation.utils.logger import setup_logger
from automation.utils.data_generator import fake

logger = setup_logger("TestLogin")

# We define the scenarios without concrete data, and resolve them in the test using real_test_user.
login_scenarios = [
    {"test_id": "LOGIN_REAL_01", "type": "valid", "expected": "success"},
    {"test_id": "LOGIN_REAL_02", "type": "wrong_password", "expected": "Invalid email or password"},
    {"test_id": "LOGIN_REAL_03", "type": "unregistered_email", "expected": "Invalid email or password"},
    {"test_id": "LOGIN_REAL_04", "type": "empty_password", "expected": "Password is required"},
]

@pytest.mark.regression
@pytest.mark.parametrize("scenario", login_scenarios, ids=lambda s: s["test_id"])
def test_dynamic_login(scenario, real_test_user, login_page, goto_login, driver):
    """
    Uses the REAL test user created in the database and applies dynamic scenarios.
    """
    email = real_test_user["email"]
    password = real_test_user["password"]

    if scenario["type"] == "wrong_password":
        password = fake.password(length=12) # Generate completely random wrong password
    elif scenario["type"] == "unregistered_email":
        email = fake.email() # Generate real-looking but unregistered email
    elif scenario["type"] == "empty_password":
        password = ""

    logger.info(f"Running {scenario['test_id']}: Type -> {scenario['type']}")
    
    login_page.login(email, password)

    if scenario["expected"] == "success":
        assert login_page.is_dashboard_displayed(), "Expected successful login to dashboard."
        logger.info(f"✅ {scenario['test_id']} passed: Login successful.")
    else:
        assert login_page.is_login_error_displayed(), "Expected an error message but none appeared."
        error_text = login_page.get_error_message()
        assert scenario["expected"].lower() in error_text.lower(), \
            f"Expected error '{scenario['expected']}' but got '{error_text}'"
        logger.info(f"✅ {scenario['test_id']} passed: Correct error displayed.")
