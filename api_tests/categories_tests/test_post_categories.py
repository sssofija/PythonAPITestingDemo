import allure
from api_tests.categories_tests.data_categories import *
from api_tests.categories_tests.conftest import *


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

    with allure.step(f"Testing invalid case: {case_name} (data: {category_data})"):
        response = api_service_client.post_category(params=category_data, cookies=cookies)

        if response.status == 400:
            print(f"Failed to create category '{category_data['name']}' with status 400")
            print(f"Server response: {response.data}")
        elif response.status == 201:
            category_id = response.data.get('id')
            if category_id:
                created_categories_storage["invalid"].append({"name": category_data["name"], "id": category_id})
                save_categories(created_categories_storage)
            assert False, f"Test failed: Expected status 400, but category was successfully created."
        else:
            assert False, f"Test failed: Unexpected status code {response.status}"

@pytest.mark.categ
@pytest.mark.parametrize("case_name, category_data", valid_data)
@allure.suite("Categories")
@allure.sub_suite("Category Validation")
@allure.title("Valid Categories")
def test_valid_category(case_name, category_data, api_service_client, get_user1_auth_token, created_categories_storage):
    cookies = {"token": get_user1_auth_token}

    with allure.step(f"Testing valid case: {case_name} (data: {category_data})"):
        response = api_service_client.post_category(params=category_data, cookies=cookies)

        if response.status == 201:
            category_id = response.data.get('id')
            if category_id:
                created_categories_storage["valid"].append({"id": category_id, "name": category_data["name"]})
                save_categories(created_categories_storage)


