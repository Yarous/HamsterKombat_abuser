from coin_earner import CoinEarner

CE: CoinEarner = CoinEarner()
response_status_code, total_earned = CE.earn_all_coins()

match response_status_code:
    case 200:
        print(f"Ваши {total_earned} монет были зачислены на ваш счет, а энергия - списана, поздравляю!")
    case _:
        print(f"Что-то пошло не по плану, вот статус код ошибки: {response_status_code}.")
