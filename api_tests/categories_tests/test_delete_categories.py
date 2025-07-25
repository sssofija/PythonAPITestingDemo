import allure
import pytest
from api_tests.categories_tests.test_post_categories import get_created_categories

@pytest.mark.categ
@allure.parent_suite("Operations")
@allure.suite("Categories")
@allure.sub_suite("Category Deletion")
@allure.title("Delete all created categories (valid and invalid)")
def test_delete_categories(get_user1_auth_token, api_service_client):
    with allure.step("Retrieve the list of previously created categories"):
        created_categories = get_created_categories()
        invalid_cases = created_categories.get("invalid", [])
        valid_cases = created_categories.get("valid", [])

    if not invalid_cases and not valid_cases:
        allure.attach("No categories found", "No categories to delete", allure.attachment_type.TEXT)
        return

    for category in valid_cases:
        category_id = category.get("id")
        if category_id:
            delete_category_by_id(category_id, api_service_client, get_user1_auth_token, valid=True)
        else:
            allure.attach(str(category), "Skipped valid category without ID", allure.attachment_type.TEXT)

    for category in invalid_cases:
        category_id = category.get("id")
        if category_id:
            delete_category_by_id(category_id, api_service_client, get_user1_auth_token, valid=False)
        else:
            allure.attach(str(category), "Skipped invalid category without ID", allure.attachment_type.TEXT)


@allure.step("Delete category by ID: {category_id}")
def delete_category_by_id(category_id, api_service_client, get_user1_auth_token, valid: bool):
    cookies = {"token": get_user1_auth_token}
    try:
        response = api_service_client.delete_category(category_id=category_id, cookies=cookies)
        allure.attach(str(response.data), f"Response when deleting category {category_id}", allure.attachment_type.JSON)

        if response.status == 200:
            status = "successfully deleted" if valid else "deleted (invalid)"
            allure.step(f"Category with ID {category_id} {status}")
        elif response.status == 404:
            allure.step(f"Category with ID {category_id} not found")
        else:
            allure.step(f"Error deleting category {category_id}: {response.data}")
    except Exception as e:
        allure.attach(str(e), f"Exception while deleting category {category_id}", allure.attachment_type.TEXT)

@pytest.mark.categ
@allure.parent_suite("Operations")
@allure.suite("Categories")
@allure.sub_suite("Deletion Verification")
@allure.title("Verify deleted categories are no longer present")
def test_deleted_categories_are_absent(api_service_client, get_user1_auth_token):
    cookies = {'token': get_user1_auth_token}

    with allure.step("Retrieve current list of categories"):
        response = api_service_client.get_categories(cookies=cookies)
        assert response.status == 200, f"Failed to fetch categories: {response.status}, {response.formatted_response}"

    existing_categories = response.data if isinstance(response.data, list) else []
    existing_ids = {category.get("id") for category in existing_categories}

    with allure.step("Compare with previously created categories"):
        created_categories = get_created_categories()
        all_created_ids = {
            category["id"]
            for category_list in created_categories.values()
            for category in category_list
            if "id" in category
        }

        undeleted = all_created_ids & existing_ids

        if undeleted:
            allure.attach(str(undeleted), "Undeleted categories", allure.attachment_type.TEXT)

        assert not undeleted, f"The following categories were not deleted: {undeleted}"
