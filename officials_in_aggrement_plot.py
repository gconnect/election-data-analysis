import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path to your XLSX file
file_path = '/Users/gloryagatevure/Desktop/result.xlsx'

# Read the XLSX file into a DataFrame
df = pd.read_excel(file_path)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Officials in Agreement
ax.bar(df['S/N'], df['Officials in Agreement (n)'], width=0.4, label='Officials in Agreement', align='center', color='green')

# Plot Total Number of Officials
ax.bar(df['S/N'], df['Total Number of Officials (N)'], width=0.4, label='Total Number of Officials (N)', align='edge', color='orange')

# Customize the plot
plt.title('Officials in Agreement vs. Total Number of Officials')
plt.xlabel('S/N')
plt.ylabel('Count')
plt.legend()

# Show the plot
plt.show()