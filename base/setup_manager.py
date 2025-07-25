import os
from dotenv import load_dotenv


class SetupManager:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("BASE_URL")
        self.environment = os.getenv("CI_TESTING_ENV", "qa")

    def set_url(self) -> str:
        if self.environment:
            url = f"https://{self.environment}.{self.base_url.lstrip('https://')}"
        else:
            url = self.base_url
        return url

    def get_user_mail1(self) -> str:
        return os.getenv("AUTOTEST_USER1_MAIL")

    def get_user_pwd(self) -> str:
        return os.getenv("AUTOTEST_USER_PASS")

    def get_restcountries_url(self) -> str:
        return os.getenv("RESTCOUNTRIES_API_URL")

