from aiohttp_session import session
from requests_payload_sample import RequestsPayloadSample


class AllBoostsForBuy(RequestsPayloadSample):
    async def get_all_boosts_for_buy(self) -> dict:
        async with session.post("https://api.hamsterkombatgame.io/clicker/boosts-for-buy",
                                headers=self._request_headers
                                ).json() as all_buy_boosts:

            return all_buy_boosts.get("boostsForBuy")