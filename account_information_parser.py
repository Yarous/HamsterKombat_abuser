from aiohttp_session import session
from requests_payload_sample import RequestsPayloadSample


class AccountInformation(RequestsPayloadSample):
    async def get_account_info(self) -> dict:
        async with session.post("https://api.hamsterkombatgame.io/clicker/sync", 
                                headers=self._request_headers
                                ).json().get('clickerUser') as account_info:
            
            return account_info
