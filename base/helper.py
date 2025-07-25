import json
import allure
from allure_commons.types import AttachmentType


def attach_request(method, url, data=None, json_body=None):
    with allure.step(f"Request {method} {url}"):
        allure.attach(method, name="HTTP Method", attachment_type=AttachmentType.TEXT)
        allure.attach(url, name="URL", attachment_type=AttachmentType.TEXT)
        if data:
            allure.attach(json.dumps(data, indent=4, ensure_ascii=False), name="Request Data",
                          attachment_type=AttachmentType.JSON)
        if json_body:
            allure.attach(json.dumps(json_body, indent=4, ensure_ascii=False), name="JSON Body",
                          attachment_type=AttachmentType.JSON)


def attach_response(response_data, status, headers, attachment_type=AttachmentType.JSON):
    with allure.step(f"Response {status}"):
        allure.attach(str(status), name="Status Code", attachment_type=AttachmentType.TEXT)
        allure.attach(json.dumps(dict(headers), indent=4, ensure_ascii=False), name="Headers",
                      attachment_type=AttachmentType.JSON)
        allure.attach(json.dumps(response_data, indent=4, ensure_ascii=False), name="Response Body",
                      attachment_type=attachment_type)


def get_content_by_type(content_type, response):
    if 'application/json' in content_type:
        try:
            content_data = response.json()
            attach_type = AttachmentType.JSON
        except json.JSONDecodeError:
            content_data = response.text
            attach_type = AttachmentType.TEXT
    elif 'text' in content_type:
        content_data = response.text
        attach_type = AttachmentType.TEXT
    else:
        content_data = response.content
        attach_type = AttachmentType.TEXT

    return content_data, attach_type