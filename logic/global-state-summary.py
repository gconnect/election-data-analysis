import json
import csv
import matplotlib.pyplot as plt

# Load data from the JSON file
with open('/Users/gloryagatevure/Desktop/global-state-summary.json', 'r') as json_file:
    data = json.loads(json_file.read())  # Use json.loads to parse the JSON data

# Create an array to store key-value pairs
key_values = []

# Define a mapping of encoded keys to their corresponding decoded keys
key_mapping = {
    "Y2FuZGlkYXRlX2NvdW50ZXI=": "candidated_candidate",
    "cG9sbGluZ19hZ2VudF9jb3VudGVy": "polling_agent_counter",
    "cG9sbGluZ19zdGF0aW9uX2NvdW50ZXI=": "polling_station_counter",
    "c3VibWlzc2lvbl9jb3VudGVy": "submission_period",
    "c3VibWlzc2lvbl9wZXJpb2Q=": "subscription_period_counter",
}

# Loop through the global-state and decode the key, exclude "submission_period"
for item in data["params"]["global-state"]:
    encoded_key = item['key']
    value = item['value']['uint']

    # Use the mapping to find the decoded key
    decoded_key = key_mapping.get(encoded_key, encoded_key)

    # Exclude rows where the key is "submission_period"
    if decoded_key != "submission_period":
        key_values.append({'decoded_key': decoded_key, 'value': value})

    # Output key-value pairs to the console
    print(f"Decoded Key: {decoded_key}, Value: {value}")

# Write decoded key-value pairs (excluding "submission_period") to a CSV file
with open('../global-state-decoded-keys.csv', 'w', newline='') as csv_file:
    fieldnames = ['decoded_key', 'value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for kv in key_values:
        writer.writerow(kv)

# Plot a graph using Matplotlib based on decoded keys
decoded_keys = [kv['decoded_key'] for kv in key_values]
values = [kv['value'] for kv in key_values]

plt.figure(figsize=(10, 6))
plt.bar(decoded_keys, values)
plt.xlabel('Decoded Key')
plt.ylabel('Value')
plt.title('Global State Key-Value Pairs (Excluding submission_period)')
plt.xticks(rotation=90)
plt.tight_layout()

# Save the graph as an image
plt.savefig('global-state-graph-decoded-keys.png')

# Display the graph
plt.show()