import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
data = pd.read_csv('../files/filtered_transactions.csv')  # Replace 'your_dataset.csv' with the actual file path

# Convert 'round-time' column to datetime
data['round-time'] = pd.to_datetime(data['round-time'], unit='s')

# Sort the DataFrame by 'confirmed-round'
data = data.sort_values(by='confirmed-round')

# Calculate transaction confirmation time (in seconds)
data['confirmation-time'] = (data['round-time'] - data['round-time'].shift()).dt.total_seconds()

# Calculate transaction throughput (transactions per second)
data['throughput'] = 1 / data['confirmation-time']

# Visualize transaction confirmation time
plt.figure(figsize=(12, 6))
plt.plot(data['confirmed-round'], data['confirmation-time'])
plt.title('Transactions Performance Metrics')
plt.xlabel('Confirmed Round')
plt.ylabel('Confirmation Time (seconds)')
plt.grid(True)

 # Save the graph as an image
plt.savefig('../images/transaction-metric.png')
plt.show()

# Visualize transaction throughput
plt.figure(figsize=(12, 6))
plt.plot(data['confirmed-round'], data['throughput'])
plt.title('Transaction Throughput Over Rounds')
plt.xlabel('Confirmed Round')
plt.ylabel('Throughput (transactions per second)')
plt.grid(True)

# Save the graph as an image
plt.savefig('../images/transaction-throughput.png')
plt.show()


# Summary statistics
confirmation_time_mean = data['confirmation-time'].mean()
confirmation_time_median = data['confirmation-time'].median()
max_throughput = data['throughput'].max()

print(f'Mean Confirmation Time: {confirmation_time_mean:.2f} seconds')
print(f'Median Confirmation Time: {confirmation_time_median:.2f} seconds')
print(f'Max Transaction Throughput: {max_throughput:.2f} transactions per second')