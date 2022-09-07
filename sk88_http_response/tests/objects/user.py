from typing import Dict

from sk88_http_response.modules.http.interfaces.http_dict import HTTPDict


class User(HTTPDict):
    def __init__(self, first_name: str, last_name: str):
        self.__first_name: str = first_name
        self.__last_name: str = last_name

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_http_dict(self) -> Dict[str, any]:
        return {
            "first_name": self.get_first_name(),
            "last_name": self.get_last_name()
        }
