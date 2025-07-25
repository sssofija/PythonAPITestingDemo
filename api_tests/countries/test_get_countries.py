import allure
import logging
import random
from http import HTTPStatus
from base.logger import logger
from base.base_api import BaseResponseModel
from api_tests.countries.conftest import countries_list

logger = logging.getLogger(__name__)

@allure.title("Retrieving the list of countries and verifying a random country against the server response.")
@allure.label("testType", "positive")
def test_get_countries(api_service_client):
    response: BaseResponseModel = api_service_client.get_countries()
    assert response.status == HTTPStatus.OK
    assert isinstance(response.data, list)
    assert len(response.data) > 0

    random_country = random.choice(countries_list)
    assert isinstance(random_country, dict)
    assert "name" in random_country
    assert "code" in random_country

    server_country = next(
        (country for country in response.data if country["name"] == random_country["name"]),
        None
    )

    assert server_country is not None
    assert server_country["name"] == random_country["name"]
    assert server_country["code"] == random_country["code"]
    assert "id" in server_country

    print(server_country, random_country)
    logger.info(response.status)
    logger.info(response.data)
