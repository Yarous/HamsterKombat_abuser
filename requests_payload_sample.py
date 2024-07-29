import config
from fake_useragent import UserAgent
from time import time

UA = UserAgent()


class RequestsPayloadSample:

    def __init__(self):
        self._fake_useragent = UA.random
        self._authorization_key = config.authorization_key
        self._unix_timestamp = int(time())
        self._request_body = None
        self._request_headers = {
            "authorization": self._authorization_key,
            "Host": "api.hamsterkombatgame.io",
            "User-Agent": self._fake_useragent,
            "Referer": "https://hamsterkombatgame.io/",
            "content-type": "application/json",
            "Origin": "https://hamsterkombatgame.io",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Priority": "u=4",
            "TE": "trailers"
        }
