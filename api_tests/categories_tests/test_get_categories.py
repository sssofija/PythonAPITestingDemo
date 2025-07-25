import allure
from faker import Faker
from api_tests.categories_tests.conftest import *

fake = Faker()

@pytest.mark.categ
@pytest.mark.parametrize("query_params", query_params_list, ids=query_ids)
@pytest.mark.parametrize("token_name, token_label, expected_status, expect_list",
                         token_cases,
                         ids=token_ids)
@allure.parent_suite("Operations")
@allure.suite("Categories")
@allure.sub_suite("List Retrieval")
@allure.title("Check category list retrieval with different tokens and filters")
def test_get_categories_with_filters(api_service_client,
                                     request,
                                     query_params,
                                     token_name,
                                     token_label,
                                     expected_status,
                                     expect_list):
    if token_name == "get_user1_auth_token":
        token = request.getfixturevalue(token_name)
    elif token_name == "fake_token":
        token = fake.uuid4()
    else:
        token = None

    with allure.step(f"Sending request with {token_label} and query parameters: {query_params}"):
        cookies = {"token": token} if token else {}
        response = api_service_client.get_categories(cookies=cookies, params=query_params)
        allure.attach(
            str(response.formatted_response),
            name="Server Response",
            attachment_type=allure.attachment_type.JSON
        )

        assert response.status == expected_status, f"Expected {expected_status}, got {response.status}"
