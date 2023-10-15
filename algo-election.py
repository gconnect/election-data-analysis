import requests
import csv

# Define the URL to fetch data
url = "https://testnet-idx.algonode.cloud/v2/transactions?application-id=271974356"

# Make a GET request to fetch the JSON data
response = requests.get(url)
data = response.json()

# Define the list of columns to remove
columns_to_remove = [
    "close-rewards",
    "closing-amount",
    "created-apps",
    "genesis-hash",
    "receiver-reward",
    "sender-rewards",
    "created-application-index",
    "application-transaction.accounts",
    "application-transaction.foreign-apps",
    "application-transaction.foreign-assets",
    "application-transaction.global-state-schema",
    "application-transaction.local-state-schema.num-byte-slice",
    "application-transaction.local-state-schema.num-unit",
]

# Extract column names from the first transaction as headers
first_transaction = data["transactions"][0]
headers = [col for col in first_transaction.keys() if col not in columns_to_remove]

# Create a CSV file and write the data with selected columns
with open("filtered_transactions.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for transaction in data["transactions"]:
        # Remove the specified columns
        selected_data = {key: transaction[key] for key in headers}
        writer.writerow(selected_data)

print("CSV file 'filtered_transactions.csv' has been created with selected columns.")
