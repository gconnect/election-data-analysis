# Data Analysis, Interpretation And Visualization

## Graph of consensus reached and not reached

**Fig 1:1** Consensus Reached

![image](./images/consensus_reached.png)

The above plot shows a bar chart. The red bar representing **No**(Consensus not reached) and the blue representing **Yes** (Consensus reached).
The above analysis show that a greater percentage of the vote count did not reach consensus.

**X-Axis Label ("Consensus"):** This label specifies the categories being plotted on the x-axis, which are different types of consensus.

**Y-Axis Label ("Count"):** The label on the y-axis indicates that the count of occurrences is being measured.

**Interpretation:**

- This plot is a bar chart that shows the distribution of different consensus outcomes.
- It helps visualize how many times each type of consensus outcome (e.g., "Yes" or "No") has been reached in the data.
- By observing the height of the bars, you can quickly determine the frequency or count of each consensus outcome.
- The colors differentiate between different types of consensus outcomes. In this case, red and blue bars represent different consensus results, such as "Consensus Reached - Yes" and "Consensus Reached - No."

## Graph of the actual data compared to the aggregation of consensus reached

**Fig** Comparative Analysis of Actual Vote Count and Consensus Vote Count

![image](./images/vote_count_comparison.png)

**Interpretation:**

The bar on the left, labeled 'Total Vote Count,' represents the total vote count for all data in the CSV file, irrespective of whether 'Consensus Reached' is 'Yes' or not.

The bar on the right, labeled 'Total Vote Count (Consensus Reached Yes),' represents the total vote count, considering only the rows where 'Consensus Reached' is 'Yes.'

The plot allows you to visually compare these two categories of vote counts. It's a straightforward way to see how the total vote count changes when 'Consensus Reached' is 'Yes' and when it is not. The color-coding (blue and green) helps distinguish between the two categories.

This information is useful for understanding the impact of 'Consensus Reached' on the total vote count 

## Officials in agreement compared with total officials
**Fig 1:1** Officials in Agreement vs Total Officials

![image](./images/official_in_aggreement.png)

**Y-Axis (Count):** The y-axis represents the count, which measures the number of officials in agreement and the total number of officials (N).

**Y-Axis Label ("Count"):** The label on the y-axis specifies that the count is being measured.

**Legend:** The legend on the plot explains the color code for the bars. The green bars represent "Officials in Agreement," while the blue bars represent "Total Number of Officials (N)."

**Interpretation:**

- This plot provides a visual comparison between the count of officials who are in agreement and the total number of officials.
- By observing the height of the bars, it can be determined whether most officials are in agreement or if there is a significant disagreement on the vote count.
- The plot is useful for decision-makers or officials to quickly grasp the level of consensus or disagreement among a group of officials.
- If the green bars (Officials in Agreement) are close in height to the blue bars (Total Number of Officials), it indicates a high level of agreement. Conversely, if the green bars are significantly shorter, it suggests a lower level of agreement.

In summary, this plot is a visual tool for officials to assess and understand the degree of consensus or agreement among a group of officials in a clear and concise manner. 
And the above plot shows a significant level of disagreement between the officials. Which means little level of consensus was reached.



## Performance/ traffic/ Saturation/Latency  Analysis

### Transaction Performance Metric Analysis

**Fig:** Transaction Metrics

![image](./images/transaction-metric.png)
The above plot visualizes the transaction confirmation time over different confirmed rounds.

**Interpretation:** 

The plot allows you to observe how the confirmation time for transactions varies over different rounds. You can look for patterns, spikes, or fluctuations in confirmation times. Sudden peaks may indicate delays in transaction processing, while valleys represent quicker confirmations.
There was a delay in the transaction at point 35000 seconds which was confirmed in 3.20 confirmed rounds.

### Transaction Throughput Over Rounds Analysis

**Fig** Transaction Throughput
![image](./images/transaction-throughput.png)
The above plot visualizes transaction throughput over different confirmed rounds

**Interpretation:**

The above plot helps you understand the capacity of the system to process transactions. It shows how many transactions were confirmed per second during different rounds. Higher peaks indicate better throughput, while lower values may suggest congestion or reduced processing capacity.


### Saturation Analysis

Saturation refers to the point at which a network reaches its processing capacity. The saturation analysis checks for network's capacity and congestion.

**Fig:** Saturation Analysis

![image](./images/saturation.png)

The above plot shows a line graph, where each point on the line corresponds to a specific timestamp (time) and its associated transaction fee. The points are marked with circular markers ("o") connected by lines ("-"). This visualization method allows you to track changes in transaction fees over time.

**X-Axis (Timestamp):** The x-axis represents time in the form of timestamps. It shows when the transactions were confirmed. This axis allows you to track the progression of time.

**Y-Axis (Transaction Fee in Algos):** The y-axis represents the transaction fee in Algos. It quantifies the cost associated with each transaction. Transaction fees are typically used to incentivize network nodes to process and confirm transactions.

**Title ("Saturation Analysis"):** The title of the plot indicates that it is related to saturation analysis. 

**Interpretation:**

- The plot provides an overview of how transaction fees change over time. It can help you identify trends and patterns in transaction fees on the blockchain network.

- Rising transaction fees might indicate increased demand for network resources, potentially suggesting network congestion.

- Falling transaction fees may indicate reduced demand or improved network efficiency.

- Sudden spikes in transaction fees could be linked to particular events, such as a surge in network usage or the introduction of new applications or assets on the blockchain.

- A consistent flat line could suggest stability in the network with relatively constant transaction fees.

The above Saturation Analysis plot shows a consistent flat transaction fee across different timestamp and transactions. This suggest stability in the Algorand network.
Understanding how transaction fees change over time is essential for blockchain users, developers, and network operators to make informed decisions and adapt to changing conditions on the network. The visualization can also be useful for forecasting and optimizing transaction costs.

### Latency Analysis

![image](./images/latency.png)

This plot helps in understanding the latency in the confirmation of transactions over a period.
The plot is a line graph, with each data point represented as a circular marker ("o") connected by lines ("-"). This visualization method allows you to track changes in latency over time.

Interpretation:

- The plot provides insights into the latency experienced by transactions on the blockchain network.

- An upward trend in latency suggests that transaction confirmation times are increasing, which might indicate network congestion or increased demand.

- A downward trend in latency indicates decreasing confirmation times, potentially due to network optimization or reduced demand.

- Spikes in latency might be linked to specific events or congestion periods when transactions are taking longer to confirm.

- Consistent, stable latency indicates that the network is maintaining a relatively constant confirmation time.

- Fluctuations in latency can reveal patterns and help users and developers understand the performance of the blockchain network at different times.

This plot is valuable for assessing the efficiency and responsiveness of the blockchain network in processing transactions. Monitoring and analyzing latency trends can assist in making informed decisions about when to submit transactions to achieve desired confirmation times and to identify periods of network stress or congestion.

The above plot indicate an upward trend in latency which suggest that confirmation times are increasing, which might indicate network congestion or increased demand.

### Traffic Analysis

This type of plot is useful for understanding transaction behavior and identifying trends or anomalies in the dataset over time. It can be helpful for monitoring network activity, identifying peak usage times, or analyzing the impact of specific events on transaction traffic.

**Fig:** Traffic Analysis

![image](./images/traffic.png)
The above plot counts the number of transactions in each round and plots the results as a line chart. Here's an interpretation of the plot:

**X-Axis (Confirmed Round):** This represents the "confirmed round" of the transactions, which appears to be a measure of time or sequence of events. As the confirmed round increases, it indicates the progression of time or the order in which transactions were confirmed.

**Y-Axis (Number of Transactions):** This axis represents the number of transactions that were confirmed in each round. It measures the intensity of transaction activity during each round.

**Title ("Transactions Traffic"):** The title of the plot provides an overall description of what the plot is visualizing. In this case, it's showing the traffic or activity related to transactions.

**Interpretation:** 

The plot shows how the number of transactions varies over time (confirmed rounds). You can see patterns, spikes, or fluctuations in transaction activity. For example, if there are sudden peaks in the graph, it suggests moments of high transaction activity, while flat regions indicate periods with lower transaction volumes. The above graph shows flat regions which indicate moments of low transactions.

**Grid Lines:** The grid lines help in reading the values more accurately and are present in both the X and Y axes.


## Graph of total polling station, total polling agent, total candidate, total vote count

The plot below shows the bar chart of transaction trends across different categories and their respective values in the y-axis.
It helps in identifying patterns or trends within the data and allows users to assess how different categories are distributed or how their values have evolved over time.

**Fig:** Election data (Blockchain Inputted Data)

![image](./images/global_state_graph_filtered.png)

- The `candidate_counter` represents the total number of registered candidates
- The `polling_agent_counter` represents the total registered polling agents
- The `polling_station_counter` represents the total registered polling stations
- The `submission_counter` represents the total number of vote counts
