import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
csv_file_path = '../files/filtered_transactions.csv'  # Replace with the actual file path
df = pd.read_csv(csv_file_path)

# Convert 'round-time' and 'confirmed-round' to datetime
df['round-time'] = pd.to_datetime(df['round-time'], unit='s')
df['confirmed-round'] = pd.to_datetime(df['confirmed-round'], unit='s')

# Calculate latency
df['latency'] = (df['round-time'] - df['confirmed-round']).dt.total_seconds()

# Plot a graph to visualize latency
plt.figure(figsize=(10, 6))
plt.plot(df['confirmed-round'], df['latency'], marker='o', linestyle='-', color='b')
plt.title('Latency Over Time')
plt.xlabel('Confirmed Round')
plt.ylabel('Latency (seconds)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

 # Save the graph as an image
plt.savefig('../images/latency.png')

# Show the graph
plt.show()