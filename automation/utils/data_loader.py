import json
import os

DATA_DIR = "test_data"

def load_test_data(filename: str):
    """Loads a JSON file from the test_data directory."""
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Test data file not found: {filepath}")
    with open(filepath, 'r') as f:
        return json.load(f)
