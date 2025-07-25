import json
import allure
import requests
from jsonschema import validate
from pydantic.v1.schema import schema

from base.helper import attach_request, attach_response, get_content_by_type
from base.api_routes import api_routes


class BaseResponseModel:
    def __init__(self, status: int, data=None, headers: dict = None, formatted_response: str = None):
        self.status = status
        self.data = data
        self.headers = headers
        self.formatted_response = formatted_response


class BaseClient:
    def __init__(self, base_url: str, **kwargs):
        self.base_url = base_url
        self.kwargs = kwargs

    def custom_request(self, method: str = "POST", rout: str = "", schema: dict = None, **kwargs) -> BaseResponseModel:
        url = f"{self.base_url}{rout}"
        with allure.step(f"{method} {url}"):
            attach_request(method, url, kwargs.get('data', None), kwargs.get('json', None))
            response = requests.request(method, url, verify=False, **kwargs)

            content_type = response.headers.get('Content-Type')
            content_data, attach_type = get_content_by_type(content_type, response)
            formatted_response = json.dumps(content_data, indent=4, ensure_ascii=False)

            attach_response(content_data, response.status_code, response.headers, attach_type)

            if schema:
                validate(instance=content_data, schema=schema)

            return BaseResponseModel(status=response.status_code, data=content_data, headers=response.headers,
                                     formatted_response=formatted_response)

    def post(self, rout: str = "", data: dict = None, json: dict = None, schema: dict = None,
             files: dict = None, cookies: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("POST", rout, schema, data=data, json=json, files=files, cookies=cookies,
                                   **kwargs)

    def get(self, rout: str = "", schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("GET", rout, schema, **kwargs)

    def put(self, rout: str = "", data: dict = None, schema: dict = None, json: dict = None,
            **kwargs) -> BaseResponseModel:
        return self.custom_request("PUT", rout, schema, data=data, json=json, **kwargs)

    def delete(self, rout: str = "", schema: dict = None, json: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("DELETE", rout, schema, json=json, **kwargs)

    def patch(self, rout: str = "", data: dict = None, json: dict = None, schema: dict = None,
              **kwargs) -> BaseResponseModel:
        return self.custom_request("PATCH", rout, schema, data=data, json=json, **kwargs)

    def head(self, rout: str = "", schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.custom_request("HEAD", rout, schema, **kwargs)


class ApiServiceClient(BaseClient):

    # Categories
    def get_categories(self,
                       cookies: dict = None,
                       **kwargs
                       ) -> BaseResponseModel:
        return self.get(api_routes['categories']['get_categories'],
                        cookies = cookies,
                        **kwargs
                        )

    def post_category(self,
                      params: dict = None,
                      schema: dict = None,
                      **kwargs
                      ) -> BaseResponseModel:
        return self.post(api_routes['categories']['post_categories'],
                         json=params,
                         schema=schema,
                         **kwargs)

    def update_category(self, category_id: int,
                        params: dict = None,
                        schema: dict = None,
                        **kwargs) -> BaseResponseModel:
        return self.put(api_routes['categories']['put_categories_id'].format(category_id),
                        json=params,
                        schema=schema,
                        **kwargs)

    def patch_category(self, category_id: int, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.patch(api_routes['categories']['patch_categories_id'].format(category_id), json=params, schema=schema, **kwargs)

    def delete_category(self,
                        category_id: int,
                        **kwargs,
                        ) -> BaseResponseModel:
        return self.delete(api_routes['categories']['delete_categories_id'].format(category_id),
                           **kwargs
                           )

        # Countries
    def get_countries(self) -> BaseResponseModel:
        return self.get(api_routes['countries']['get_countries'])


    # Operations
    def get_operations(self) -> BaseResponseModel:
        return self.get(api_routes['operations']['get_operations'])

    def post_operation(self, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.post(api_routes['operations']['post_operations'], json=params, schema=schema, **kwargs)

    def get_operation(self, operation_id: int) -> BaseResponseModel:
        return self.get(api_routes['operations']['get_operations_id'].format(operation_id))

    def update_operation(self, operation_id: int, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.put(api_routes['operations']['put_operations_id'].format(operation_id), json=params, schema=schema, **kwargs)

    def patch_operation(self, operation_id: int, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.patch(api_routes['operations']['patch_operations_id'].format(operation_id), json=params, schema=schema, **kwargs)

    def delete_operation(self, operation_id: int) -> BaseResponseModel:
        return self.delete(api_routes['operations']['delete_operations_id'].format(operation_id))

    # Password
    def get_password_reset_confirm(self) -> BaseResponseModel:
        return self.get(api_routes['password']['get_password_reset_confirm'])

    # Profile
    def get_profile(self) -> BaseResponseModel:
        return self.get(api_routes['profile']['get_profile'])

    def update_profile(self, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.patch(api_routes['profile']['patch_profile'], json=params, schema=schema, **kwargs)

    # Targets
    def get_targets(self) -> BaseResponseModel:
        return self.get(api_routes['targets']['get_targets'])

    def post_target(self, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.post(api_routes['targets']['post_targets'], json=params, schema=schema, **kwargs)

    def update_target(self, target_id: int, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.put(api_routes['targets']['put_targets_id'].format(target_id), json=params, schema=schema, **kwargs)

    def patch_target(self, target_id: int, params: dict = None, schema: dict = None, **kwargs) -> BaseResponseModel:
        return self.patch(api_routes['targets']['patch_targets_id'].format(target_id), json=params, schema=schema, **kwargs)

    def delete_target(self, target_id: int) -> BaseResponseModel:
        return self.delete(api_routes['targets']['delete_targets_id'].format(target_id))

    def delete_target_return_money(self, target_id: int) -> BaseResponseModel:
        return self.delete(api_routes['targets']['delete_targets_id_return_money'].format(id=target_id))

    def get_target_by_id(self, target_id: int) -> BaseResponseModel:
        return self.get(api_routes['targets']['get_targets_by_id'].format(target_id))