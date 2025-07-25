import json
import pytest


STORAGE_FILE = "created_categories.json"

def save_categories(data):
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_categories():
    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"invalid": [], "valid": []}

_created_categories_storage = load_categories()

@pytest.fixture(scope="session")
def created_categories_storage():
    return _created_categories_storage

def get_created_categories():
    return load_categories()

query_params_list = [
    {"is_outcome": "true"},
    {"is_income": "true"},
    {"is_outcome": "false"},
    {"is_income": "false"},
    {"is_outcome": "true", "is_income": "true"},
    {"is_outcome": "false", "is_income": "false"},
    {"is_outcome": "true", "is_income": "false"},
    {"is_outcome": "false", "is_income": "true"},
    {},
]

query_ids = [
    "Outcome True",
    "Income True",
    "Outcome False",
    "Income False",
    "Outcome+Income True",
    "Outcome+Income False",
    "Outcome True + Income False",
    "Outcome False + Income True",
    "No Filters"
]

token_cases = [
    ("get_user1_auth_token", "valid token", 200, True),
    ("fake_token", "invalid token", 401, False),
    (None, "no token", 401, False),
]

token_ids = [
    "Valid Token",
    "Invalid Token",
    "No Token"
]
def save_created_category(storage: dict, category_type: str, category_id: str, name: str):
    storage[category_type].append({"id": category_id, "name": name})
    save_categories(storage)
