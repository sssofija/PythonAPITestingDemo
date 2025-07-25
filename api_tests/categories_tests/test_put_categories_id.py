import allure
import pytest
from api_tests.categories_tests.test_post_categories import get_created_categories

@pytest.mark.categ
@allure.parent_suite("Operations")
@allure.suite("Categories")
@allure.sub_suite("Category Update")
@allure.title("Update all previously created categories (valid and invalid)")
def test_update_categories(api_service_client, get_user1_auth_token):
    with allure.step("Retrieve the list of previously created categories"):
        created_categories = get_created_categories()
        invalid_cases = created_categories.get("invalid", [])
        valid_cases = created_categories.get("valid", [])

    if not invalid_cases and not valid_cases:
        allure.attach("No categories found", "No categories to update", allure.attachment_type.TEXT)
        return

    for category in valid_cases:
        category_id = category.get("id")
        if category_id:
            update_category_by_id(category_id, api_service_client, get_user1_auth_token, valid=True)
        else:
            allure.attach(str(category), "Skipped valid category without ID", allure.attachment_type.TEXT)

    for category in invalid_cases:
        category_id = category.get("id")
        if category_id:
            update_category_by_id(category_id, api_service_client, get_user1_auth_token, valid=False)
        else:
            allure.attach(str(category), "Skipped invalid category without ID", allure.attachment_type.TEXT)


@allure.step("Update category by ID: {category_id}")
def update_category_by_id(category_id, api_service_client, get_user1_auth_token, valid: bool):
    cookies = {"token": get_user1_auth_token}
    params = {"is_deleted": False}

    try:
        response = api_service_client.update_category(category_id=category_id, params=params, cookies=cookies)
        allure.attach(str(response.data), f"Server response when updating ID {category_id}", allure.attachment_type.JSON)

        if response.status == 200:
            message = "successfully updated" if valid else "updated (invalid)"
            allure.step(f"Category with ID {category_id} {message}")
        else:
            allure.step(f"Error updating category {category_id}: {response.data}")

    except Exception as e:
        allure.attach(str(e), f"Exception while updating category {category_id}", allure.attachment_type.TEXT)
