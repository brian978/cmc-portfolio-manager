import json
import os
from time import sleep

from dotenv import load_dotenv
import requests

from payload_converter import eth, from_cg_to_cmc, btc, dot, near, egld, ftm, solana, avax, axie

load_dotenv()

# Read transactions from JSON file
with open('transactions.json') as file:
    data = json.load(file)
    transactions = data['transactions']

# API endpoint URL
api_url = 'https://api.coinmarketcap.com/asset/v3/portfolio/add'  # Replace with your API endpoint URL

# Bearer token for authentication
bearer_token = os.getenv('BEARER_TOKEN')  # Replace with your bearer token

# Iterate over transactions and make POST requests
for transaction in transactions:
    if transaction['transaction_type'] == 'transfer_in' or transaction['transaction_type'] == 'transfer_out':
        continue

    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }

    payload = from_cg_to_cmc(axie(), transaction)
    response = requests.post(api_url, json=payload, headers=headers)

    print(payload)

    if response.status_code == 200:
        print(f"Transaction {transaction['id']} successfully sent to the API.")
        print(response.text)
    else:
        print(f"Failed to send transaction {transaction['id']} to the API. Error: {response.text}")

    sleep(20)
