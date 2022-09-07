from typing import Dict


class HTTPDict:
    """ Interface for HTTP dictionary objects
    """

    def get_http_dict(self) -> Dict[str, any]:
        """ Get HTTP dict
        Returns:
            Dict[str, any]
        """
        pass
