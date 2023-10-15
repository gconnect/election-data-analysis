import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path to your XLSX file
file_path = '/Users/gloryagatevure/Desktop/result.xlsx'

# Read the XLSX file into a DataFrame
df = pd.read_excel(file_path)

# Filter rows where 'Consensus Reached' is 'yes'
consensus_yes = df[df['Consensus Reached'] == 'yes']

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Total Number of Officials
ax.bar(df['S/N'], df['Total Number of Officials (N)'], width=0.4, label='Total Number of Officials (N)', align='edge', color='blue', alpha=0.5)

# Plot Total Number of Officials in Agreement
ax.bar(consensus_yes['S/N'], consensus_yes['Total Number of Officials (N)'], width=0.4, label='Total Officials in Agreement (Consensus)', align='center', color='green')

# Customize the plot
plt.title('Total Number of Officials vs. Total Officials in Agreement (Consensus)')
plt.xlabel('S/N')
plt.ylabel('Count')
plt.legend()

# Show the plot
plt.show()