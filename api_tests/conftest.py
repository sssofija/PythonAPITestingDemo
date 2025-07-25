import pytest
import requests
from api_tests.auth_tests.routs import auth_api_routes
from base.logger import logger
from base.setup_manager import SetupManager
from base.base_api import ApiServiceClient
import random
from http import HTTPStatus


@pytest.fixture(scope="session")
def setup_manager():
    return SetupManager()

@pytest.fixture(scope="session")
def set_url(setup_manager):
    return setup_manager.set_url()

@pytest.fixture(scope="session")
def set_user1_mail(setup_manager):
    return setup_manager.get_user_mail1()

@pytest.fixture(scope="session")
def set_user_pwd(setup_manager):
    return setup_manager.get_user_pwd()

@pytest.fixture(scope="session")
def get_user1_auth_token(set_url, set_user1_mail, set_user_pwd):
    response = requests.post(
        url=f'{set_url}{auth_api_routes["auth"]["post_login"]}',
        json={
            "password": set_user_pwd,
            "email": set_user1_mail
        }
    )
    try:
        return response.json()['auth_token']
    except KeyError:
        logger.error("auth_token not found in response")
        return None

@pytest.fixture(scope="session")
def get_random_user_id(auth_api_client,
                       get_user1_auth_token):
    response = auth_api_client.get_auth_users(cookies={"token": get_user1_auth_token})
    random_user = random.choice(response.data)
    if random_user:
        return random_user['id']
    else:
        logger.info("user data is empty")

@pytest.fixture(scope="session")
def api_service_client(set_url):
    return ApiServiceClient(base_url=set_url)

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