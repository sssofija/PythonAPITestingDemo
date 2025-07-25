import pytest
import logging
from base.base_api import BaseClient
import requests
from typing import List, Dict
from base.setup_manager import SetupManager

logger = logging.getLogger(__name__)

def fetch_all_countries() -> List[Dict]:
    setup = SetupManager()
    url = setup.get_restcountries_url()
    response = requests.get(url)
    return response.json()


def get_country_name(country: dict) -> str:
    name_rus = country.get("translations", {}).get("rus", {}).get("common")
    name = name_rus if isinstance(name_rus, str) else country["name"]["common"]
    return name.upper()


countries = fetch_all_countries()

formatted_countries = [
    {
        "id": i + 1,
        "name": get_country_name(country),
        "code": country.get("cca2", "")
    }
    for i, country in enumerate(countries)
]

countries_list = formatted_countries


@pytest.fixture(scope="session")
def auth_api_client(set_url):
    return BaseClient(base_url=set_url)


