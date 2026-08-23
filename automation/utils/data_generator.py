from faker import Faker
import random

fake = Faker()

def generate_real_user():
    """Generates a highly realistic user persona on the fly."""
    return {
        "username": fake.user_name() + str(random.randint(1000, 9999)),
        "email": fake.email(),
        "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    }

def get_registration_scenarios():
    """Generates dynamic registration scenarios using real-looking data."""
    return [
        {
            "test_id": "REG_REAL_01",
            "desc": "Valid Registration with Real Persona",
            "user": generate_real_user(),
            "expected": "success"
        },
        {
            "test_id": "REG_REAL_02",
            "desc": "Invalid Email Format (Real email with @ stripped)",
            "user": {
                "username": generate_real_user()["username"],
                "email": generate_real_user()["email"].replace("@", ""),
                "password": generate_real_user()["password"]
            },
            "expected": "Invalid email format"
        },
        {
            "test_id": "REG_REAL_03",
            "desc": "Password too short",
            "user": {
                "username": generate_real_user()["username"],
                "email": generate_real_user()["email"],
                "password": "pass" # Intentionally short
            },
            "expected": "Password must be at least 6 characters"
        },
        {
            "test_id": "REG_REAL_04",
            "desc": "Empty Username",
            "user": {
                "username": "",
                "email": generate_real_user()["email"],
                "password": generate_real_user()["password"]
            },
            "expected": "Username must be at least 3 characters"
        }
    ]
