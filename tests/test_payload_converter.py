import unittest
import dotenv

from payload_converter import btc, from_cg_to_cmc, eth


class PayloadConverterCase(unittest.TestCase):
    def setUp(self) -> None:
        self.env = dotenv.dotenv_values()

    def test_converts_buy_transaction(self):
        source = {
            "id": 1,
            "fees": "1.0",
            "price": "100",
            "proceeds": "0.0",
            "cost": "125",
            "transaction_type": "buy",
            "profit_loss": 113,
            "date": "05 Jan 2011 05:42 AM UTC"
        }

        expected = {
            "amount": "1.25",
            "price": "100",
            "transactionTime": '2011-01-05T05:42:00.000Z',
            "fee": "1.0",
            "note": "",
            "transactionType": "buy",
            "cryptocurrencyId": 1,
            "cryptoUnit": 2781,
            "fiatUnit": 2781,
            "portfolioSourceId": self.env['PORTFOLIO_ID']
        }

        self.assertEqual(expected, from_cg_to_cmc(btc(), source))

    def test_converts_sell_transaction(self):
        source = {
            "id": 1,
            "fees": '',
            "price": 987.6245870533292,
            "proceeds": "126.486211812918033792708",
            "cost": "0.0",
            "transaction_type": "sell",
            "profit_loss": 0,
            "date": "05 Jan 2011 08:20 AM UTC"
        }

        expected = {
            "amount": "0.12807114512033518",
            "price": "987.6245870533292",
            "transactionTime": "2011-01-05T08:20:00.000Z",
            "fee": "",
            "note": "",
            "transactionType": "sell",
            "cryptocurrencyId": 1027,
            "cryptoUnit": 2781,
            "fiatUnit": 2781,
            "portfolioSourceId": self.env['PORTFOLIO_ID']
        }

        self.assertEqual(expected, from_cg_to_cmc(eth(), source))
