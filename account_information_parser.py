import requests
from requests_payload_sample import RequestsPayloadSample


class AccountInformation(RequestsPayloadSample):

    def get_account_info(self) -> dict:
        response = requests.post("https://api.hamsterkombatgame.io/clicker/sync", headers=self._request_headers)
        return response.json()['clickerUser']
