from aiohttp_session import session
from requests_payload_sample import RequestsPayloadSample


class ClickerConfigParser(RequestsPayloadSample):
    def __init__(self):
        super().__init__()

    async def get_clicker_config(self) -> dict:
        async with session.post("https://api.hamsterkombatgame.io/clicker/config",
                                 headers=self._request_headers
                                 ).json() as clicker_config:

            return clicker_config
