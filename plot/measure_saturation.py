import matplotlib.pyplot as plt
import pandas as pd

# Load data from a CSV file
file_path = '../files/filtered_transactions.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

# Convert round to timestamp (for simplicity)
df['timestamp'] = pd.to_datetime(df['confirmed-round'], unit='s')

# Plot transaction count
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['fee'], marker='o', linestyle='-')
plt.title('Saturation Analysis')
plt.xlabel('Timestamp')
plt.ylabel('Transaction Fee (Algos)')
plt.grid(True)
plt.tight_layout()

 # Save the graph as an image
plt.savefig('../images/saturation.png')

# Customize this to save or display the plot
plt.show()






