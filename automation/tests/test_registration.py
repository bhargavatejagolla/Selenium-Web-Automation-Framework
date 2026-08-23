import pytest
from automation.utils.data_generator import get_registration_scenarios
from automation.utils.logger import setup_logger

logger = setup_logger("TestRegistration")

# Get dynamically generated real data
reg_data = get_registration_scenarios()

@pytest.mark.regression
@pytest.mark.parametrize("data", reg_data, ids=lambda d: d["test_id"])
def test_dynamic_registration(data, register_page, goto_register, driver):
    """
    Tests registration using 100% dynamic, real-looking data.
    """
    user = data["user"]
    logger.info(f"Running {data['test_id']}: {data['desc']}")
    logger.info(f"Generated Persona -> Username: {user['username']}, Email: {user['email']}")

    register_page.register(user["username"], user["email"], user["password"])

    if data["expected"] == "success":
        assert register_page.is_registration_successful(), "Expected successful registration redirect to login."
        logger.info(f"✅ {data['test_id']} passed: Registration successful.")
    else:
        assert register_page.is_registration_error_displayed(), "Expected an error message but none appeared."
        error_text = register_page.get_error_message()
        assert data["expected"].lower() in error_text.lower(), \
            f"Expected error '{data['expected']}' but got '{error_text}'"
        logger.info(f"✅ {data['test_id']} passed: Correct error displayed.")
