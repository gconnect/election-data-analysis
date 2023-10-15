import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path to your XLSX file
file_path = '../files/result.csv'

# Read the XLSX file into a DataFrame
df = pd.read_csv(file_path)

# Count the occurrences of 'Consensus Reached'
consensus_counts = df['Consensus Reached'].value_counts()

# Plot the graph
consensus_counts.plot(kind='bar', color=['red', 'blue'])

# Customize the plot
plt.title('Consensus Reached')
plt.xlabel('Consensus')
plt.ylabel('Count')

# Save the graph as an image
plt.savefig('../images/consensus_reached.png')
# Show the plot
plt.show()