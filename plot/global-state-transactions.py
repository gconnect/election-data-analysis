import requests
import pandas as pd
import base64
import matplotlib.pyplot as plt

# Define the API endpoint
url = "https://testnet-idx.algonode.cloud/v2/transactions?application-id=271974356"

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Create an empty list to store the table data
table_data = []
# Initialize a counter for the total transactions
total_transactions = 0

# Loop through transactions and global-state-delta
for transaction in data["transactions"]:
    # Increment the total transactions counter
    total_transactions += 1

    for delta in transaction["global-state-delta"]:
        key = base64.b64decode(delta["key"]).decode('utf-8')  # Decode the base64 key
        uint_value = delta["value"]["uint"]

        # Exclude rows with the key "submission_period"
        if key == "submission_period":
            continue

        # Check if the uint value is a big integer (greater than a certain threshold)
        if uint_value > 1000000000:
            # Convert the uint value to a local timestamp
            timestamp = pd.to_datetime(uint_value, unit='s', origin='unix', utc=True, errors='coerce').tz_convert(
                'US/Eastern')
            table_data.append([key, timestamp])
        else:
            table_data.append([key, uint_value])

# Create a DataFrame from the table data
df = pd.DataFrame(table_data, columns=["Categories", "Value"])

# Export the DataFrame to a CSV file
df.to_csv("../files/global_state_delta_filtered.csv", index=False)

# Plot a graph using Matplotlib based on the modified data
plt.figure(figsize=(10, 6))
plt.bar(df["Categories"], df["Value"])
plt.xlabel('Categories')
plt.ylabel('Value')
plt.title('Election Data (Blockchain)')
plt.xticks(rotation=90)
plt.tight_layout()

# Save the graph as an image
plt.savefig('../images/global_state_graph_filtered.png')

print("Total Transactions:", total_transactions)

# Print the resulting DataFrame
print(df)