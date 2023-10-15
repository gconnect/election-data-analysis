import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path to your XLSX file
file_path = '../files/result.csv'

# Read the XLSX file into a DataFrame
df = pd.read_excel(file_path)

# Filter rows where 'Consensus Reached' is 'yes'
consensus_yes = df[df['Consensus Reached'] == 'yes']

# Calculate the national aggregate of vote count for 'Consensus Reached' == 'yes'
national_aggregate = consensus_yes['Vote Count'].sum()

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Total Number of Officials
ax.bar(df['S/N'], df['Officials in Agreement (n)'], width=0.4, label='Officials in Agreement (n)', align='edge', color='blue', alpha=0.5)

# Plot National Aggregate for 'Consensus Reached' == 'yes'
ax.bar(consensus_yes['S/N'], national_aggregate, width=0.4, label='National Aggregate (Consensus)', align='center', color='green')

# Customize the plot
plt.title('Officials in Agreement vs. National Aggregate (Consensus Vote Count)')
plt.xlabel('S/N')
plt.ylabel('Count')
plt.legend()


# Save the graph as an image
plt.savefig('../images/consensus_vote_count.png')

# Show the plot
plt.show()





