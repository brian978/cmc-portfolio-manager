import os

from format_date import format_date


def btc() -> dict:
    return {'cryptocurrencyId': 1, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def eth() -> dict:
    return {'cryptocurrencyId': 1027, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def dot() -> dict:
    return {'cryptocurrencyId': 6636, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def near() -> dict:
    return {'cryptocurrencyId': 6535, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def egld() -> dict:
    return {'cryptocurrencyId': 6892, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def ftm() -> dict:
    return {'cryptocurrencyId': 3513, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def solana() -> dict:
    return {'cryptocurrencyId': 5426, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def avax() -> dict:
    return {'cryptocurrencyId': 5805, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def axie() -> dict:
    return {'cryptocurrencyId': 6783, 'cryptoUnit': 2781, 'fiatUnit': 2781}


def from_cg_to_cmc(crypto: dict, payload: dict):
    transaction_type = payload['transaction_type']

    if transaction_type == 'buy':
        amount = float(payload['cost']) / float(payload['price'])
    else:
        amount = float(payload['proceeds']) / float(payload['price'])

    return {
        'amount': str(amount),
        'price': str(payload['price']),
        'transactionTime': format_date(payload['date']),
        'fee': str(payload['fees']),
        'note': '',
        'transactionType': transaction_type,
        'cryptocurrencyId': crypto['cryptocurrencyId'],
        'cryptoUnit': crypto['cryptoUnit'],
        'fiatUnit': crypto['fiatUnit'],
        'portfolioSourceId': os.getenv('PORTFOLIO_ID')
    }
