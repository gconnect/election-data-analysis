import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
data = pd.read_csv('../files/filtered_transactions.csv')  # Replace 'your_dataset.csv' with the actual file path

# Convert 'round-time' column to datetime
data['round-time'] = pd.to_datetime(data['round-time'], unit='s')

# Group transactions by confirmed round and count them
transaction_counts = data.groupby('confirmed-round').size()

# Plot the transaction counts over rounds
plt.figure(figsize=(12, 6))
plt.plot(transaction_counts.index, transaction_counts.values)
plt.title('Transactions Traffic')
plt.xlabel('Confirmed Round')
plt.ylabel('Number of Transactions')
plt.grid(True)

 # Save the graph as an image
plt.savefig('../images/traffic.png')

plt.show()