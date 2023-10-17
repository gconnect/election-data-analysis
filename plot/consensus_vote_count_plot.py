import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path to your CSV file
file_path = '../files/result.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Calculate the total Vote Count for all rows
total_vote_count = df['Vote Count'].sum()

# Filter the DataFrame to include only rows where 'Consensus Reached' is 'Yes'
consensus_yes_df = df[df['Consensus Reached'] == 'Yes']

# Calculate the total Vote Count when 'Consensus Reached' is 'Yes'
consensus_yes_vote_count = df[df['Consensus Reached'] == 'yes']['Vote Count'].sum()

# Create a DataFrame for the comparative analysis
comparison_data = pd.DataFrame({
    'Category': ['Total Vote Count', 'Total Vote Count (Consensus Reached Yes)'],
    'Count': [total_vote_count, consensus_yes_vote_count]
})

# Plot the graph as a bar chart with annotated values
plt.figure(figsize=(8, 6))
bars = plt.bar(comparison_data['Category'], comparison_data['Count'], color=['blue', 'green'])
plt.title('Comparative Analysis of Total Vote Count vs. Total Vote Count (Consensus Reached Yes)')
plt.xlabel('Category')
plt.ylabel('Count')

# Annotate the values at the top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom', fontsize=12)

# Save the graph as an image
plt.savefig('../images/vote_count_comparison.png')

# Show the plot
plt.show()