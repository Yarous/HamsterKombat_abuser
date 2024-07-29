import requests
from requests_payload_sample import RequestsPayloadSample
from account_information_parser import AccountInformation

ACINFO = AccountInformation()


class CoinEarner(RequestsPayloadSample):

    def __init__(self):
        super().__init__()
        self.total_earned = ACINFO.get_account_info()['availableTaps']
        self._request_body = {
            "count": self.total_earned,
            "availableTaps": 0,
            "timestamp": self._unix_timestamp
        }

    def earn_all_coins(self) -> requests.status_codes:
        response = requests.post("https://api.hamsterkombatgame.io/clicker/tap",
                                 headers=self._request_headers,
                                 json=self._request_body
                                 )

        return response.status_code, self.total_earned
