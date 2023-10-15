import os
import pandas as pd
import random

# Specify the folder path where your XLS files are located
folder_path = '/Users/gloryagatevure/Desktop/election-data'

# Initialize an empty list to store the extracted data
data_list = []

# Function to calculate the percentage of agreement and check if consensus is reached
def calculate_percentage_and_consensus(n, N):
    percentage = (n / N) * 100
    consensus = 'yes' if percentage > 67 else 'no'
    return percentage, consensus

# Iterate through each XLS file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xls'):
        # Load the XLS file into a DataFrame
        xls_path = os.path.join(folder_path, filename)
        df = pd.read_excel(xls_path, header=None)  # Read without header

        # Check if 'Abbr.' and 'No. of Votes' columns exist in the DataFrame (using the 20th row)
        if 19 < len(df) and 'Abbr.' in df.iloc[19].values and 'No. of Votes' in df.iloc[19].values:
            # Extract 'Abbr.' and 'No. of Votes' columns from the XLS file (using the 20th row)
            abbr_column = df.iloc[20:, df.iloc[19].values.tolist().index('Abbr.')]
            votes_column = df.iloc[20:, df.iloc[19].values.tolist().index('No. of Votes')]

            # Set 'Voting District' to equal the filename without the '.xls' extension
            voting_district = os.path.splitext(filename)[0]

            # Calculate the total number of officials (N)
            N = len(abbr_column) + 6

            # Calculate the total number of votes (Vote Count)
            vote_count = votes_column.sum()

            # Generate a random/estimated number of officials in agreement (n)
            n = random.randint(1, N)

            # Calculate the percentage of agreement and consensus reached
            percentage, consensus = calculate_percentage_and_consensus(n, N)

            # Create a dictionary for the extracted data
            data_dict = {
                'S/N': len(data_list) + 1,
                'Polling Station ID': voting_district,
                'Total Number of Officials (N)': N,
                'Vote Count': vote_count,
                'Officials in Agreement (n)': n,
                'Percentage of Agreement (%)': percentage,
                'Consensus Reached': consensus
            }

            # Append the data dictionary to the list
            data_list.append(data_dict)
        else:
            print(f"Warning: 'Abbr.' or 'No. of Votes' column not found in {filename}")

# Create a DataFrame from the list of dictionaries
result_df = pd.DataFrame(data_list)

# Save the result DataFrame to a new Excel file
result_df.to_excel('/Users/gloryagatevure/Desktop/result.xlsx', index=False)