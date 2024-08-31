from aiohttp_session import session
from requests_payload_sample import RequestsPayloadSample
from account_information_parser import AccountInformation

ACINFO = AccountInformation()


class CoinEarner(RequestsPayloadSample):

    def __init__(self):
        super().__init__()
        self.total_earned = ACINFO.get_account_info().get('availableTaps')
        self._request_body = {
            "count": self.total_earned,
            "availableTaps": 0,
            "timestamp": self._unix_timestamp
        }

    async def earn_all_coins(self) -> int:
        async with session.post("https://api.hamsterkombatgame.io/clicker/tap",
                                 headers=self._request_headers,
                                 json=self._request_body
                                 ) as tap_info:

            return tap_info.status, self.total_earned
