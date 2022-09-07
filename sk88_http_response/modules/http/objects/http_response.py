from typing import List, Dict
from sk88_http_response.modules.http.interfaces.http_dict import HTTPDict


class HTTPResponse:
    """ Object representing HTTP response
    """

    def __init__(self, http_code: int, error_message: str, data: List[HTTPDict] = []):
        """ Constructor for HTTPResponse
        Args:
            http_code (int):        HTTP code
            error_message (str):    Error message
            data (List[HTTPDict]):  List of HTTPDict objects
        """
        self.__http_code = http_code
        self.__error_message = error_message
        self.__data = [datum.get_http_dict() for datum in data]
        self.__meta: Dict[str, any] = {}

    def set_meta(self, meta: Dict[str, any]):
        """ Set extra meta data
        Args:
            meta (Dict[str, any]):
        """
        self.__meta = meta

    def get_response(self) -> tuple:
        """ Get response as tuple
        Returns:
            tuple
        """
        if self.__http_code >= 400:
            return {
                "message": self.__error_message
            }, self.__http_code

        success_response = {
            "data": self.__data
        }
        if self.__meta:
            success_response["meta"] = self.__meta
        return success_response, self.__http_code
