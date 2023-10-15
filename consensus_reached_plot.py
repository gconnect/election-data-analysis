import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path to your XLSX file
file_path = '/Users/gloryagatevure/Desktop/result.xlsx'

# Read the XLSX file into a DataFrame
df = pd.read_excel(file_path)

# Count the occurrences of 'Consensus Reached'
consensus_counts = df['Consensus Reached'].value_counts()

# Plot the graph
consensus_counts.plot(kind='bar', color=['red', 'blue'])

# Customize the plot
plt.title('Consensus Reached')
plt.xlabel('Consensus')
plt.ylabel('Count')

# Show the plot
plt.show()