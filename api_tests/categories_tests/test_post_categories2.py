import pytest
import allure
from api_tests.categories_tests.data_categories import *
from api_tests.categories_tests.conftest import *

@pytest.mark.categ
@pytest.mark.parametrize("case_name, category_data", valid_data)
@allure.parent_suite("Operations")
@allure.suite("Categories")
@allure.sub_suite("Category Validation")
@allure.title("Valid Categories")
def test_valid_category(case_name, category_data,
                        api_service_client,
                        get_user1_auth_token,
                        created_categories_storage):
    cookies = {"token": get_user1_auth_token}

    with allure.step(f"Testing valid case: {case_name}"):
        response = api_service_client.post_category(params=category_data, cookies=cookies)

        if response.status == 201:
            category_id = response.data.get('id')
            if category_id:
                save_created_category(created_categories_storage, "valid", category_id, category_data["name"])
        else:
            assert False, f"Expected status 201, got {response.status}"


@pytest.mark.categ
@pytest.mark.parametrize("case_name, category_data", invalid_cases)
@allure.parent_suite("Operations")
@allure.suite("Categories")
@allure.sub_suite("Category Validation")
@allure.title("Invalid Categories")
def test_invalid_category(case_name,
                          category_data,
                          api_service_client,
                          get_user1_auth_token,
                          created_categories_storage):
    cookies = {"token": get_user1_auth_token}

    with allure.step(f"Testing invalid case: {case_name}"):
        response = api_service_client.post_category(params=category_data, cookies=cookies)

        if response.status == 400:
            print(f"Correctly failed to create invalid category '{category_data['name']}'")
        elif response.status == 201:
            category_id = response.data.get('id')
            if category_id:
                save_created_category(created_categories_storage, "invalid", category_id, category_data["name"])
            assert False, f"Expected status 400, but got 201 (category created)."
        else:
            assert False, f"Unexpected status: {response.status}"
