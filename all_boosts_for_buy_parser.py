import requests
from requests_payload_sample import RequestsPayloadSample


class AllBoostsForBuy(RequestsPayloadSample):
    def get_all_boosts_for_buy(self) -> dict:
        all_buy_boosts = requests.post("https://api.hamsterkombatgame.io/clicker/boosts-for-buy",
                                       headers=self._request_headers
                                       )

        return all_buy_boosts.json()['boostsForBuy']
