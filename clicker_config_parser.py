import requests
from requests_payload_sample import RequestsPayloadSample


class ClickerConfigParser(RequestsPayloadSample):
    def __init__(self):
        super().__init__()

    def get_clicker_config(self) -> dict:
        response = requests.post("https://api.hamsterkombatgame.io/clicker/config",
                                 headers=self._request_headers
                                 ).json()

        return response
