import requests

from requests_payload_sample import RequestsPayloadSample
from clicker_config_parser import ClickerConfigParser
from base64 import b64decode

GCC = ClickerConfigParser()


class DailyCipherClaimer(RequestsPayloadSample):
    def __init__(self):
        super().__init__()
        self.cipher_info = GCC.get_clicker_config()["dailyCipher"]
        self.__encoded_cipher_code = self.cipher_info["cipher"]
        self.cipher_remain_seconds = self.cipher_info["remainSeconds"]
        self.decoded_cipher_code = self.decode_security_code(self.__encoded_cipher_code)

    def claim_daily_cipher(self) -> int:
        daily_cipher_status_code = requests.post("https://api.hamsterkombatgame.io/clicker/claim-daily-cipher",
                                                 headers=self._request_headers,
                                                 json={'cipher': self.decoded_cipher_code}
                                                 ).status_code

        return daily_cipher_status_code

    @staticmethod
    def decode_security_code(security_code: str) -> str:
        security_code = security_code[:3] + security_code[3 + 1:]
        return str(b64decode(security_code).decode("utf-8"))
