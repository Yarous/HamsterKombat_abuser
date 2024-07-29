import requests

from all_boosts_for_buy_parser import AllBoostsForBuy
from requests_payload_sample import RequestsPayloadSample
from account_information_parser import AccountInformation
from random import choice

AllBoostsForBuy = AllBoostsForBuy()
ACINFO = AccountInformation()
AllBoosts = AllBoostsForBuy.get_all_boosts_for_buy()
AllAccountInfo = ACINFO.get_account_info()


class RandomBoostBuyer(RequestsPayloadSample):

    def __init__(self):
        super().__init__()
        self.__available_boosts = None
        self.__boost_id = None
        self.__enough_money = None

        match any(boost["price"] > AllAccountInfo["balanceCoins"] for boost in AllBoosts if boost["price"] > 0):
            case False:
                self.__available_boosts = [boost["id"] for boost in AllBoosts if boost["price"] > 0]

    def buy_any_boost(self) -> str | int:
        if self.__available_boosts:
            request_body_for_money_boosts = {
                "boostId": choice(self.__available_boosts),
                "timestamp": self._unix_timestamp
            }
            money_boost_status_code = requests.post("https://api.hamsterkombatgame.io/clicker/buy-boost",
                                                    headers=self._request_headers,
                                                    json=request_body_for_money_boosts
                                                    )
        else:
            return f"No money, current money = {AllAccountInfo['balanceCoins']}"

        return money_boost_status_code.status_code
