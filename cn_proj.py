import matplotlib.pyplot as plt
import re

# Initialize lists for time intervals and bandwidth
intervals = []
bandwidths = []

# Regular expression to match [SUM] lines
pattern = r'\[SUM\]\s+(\d+\.\d+)-(\d+\.\d+)\s+sec\s+[\d.]+\s+\w+\s+([\d.]+)\s+(\w+)/sec'

# Read the iperf3 output file
with open('iperf_output.txt', 'r') as file:
    for line in file:
        match = re.match(pattern, line)
        if match:
            start_time = float(match.group(1))
            end_time = float(match.group(2))
            bandwidth = float(match.group(3))
            unit = match.group(4)

            # Convert bandwidth to Gbits/sec if needed
            if unit == 'Mbits':
                bandwidth /= 1000  # Convert Mbits/sec to Gbits/sec
            elif unit == 'Kbits':
                bandwidth /= 1000000  # Convert Kbits/sec to Gbits/sec

            # Use end_time for x-axis
            intervals.append(end_time)
            bandwidths.append(bandwidth)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(intervals, bandwidths, marker='o', linestyle='-')
plt.xlabel('Time (seconds)')
plt.ylabel('Bandwidth (Gbits/sec)')
plt.title('iperf3 Bandwidth Over Time')
plt.grid(True)

# Save the plot to a file
plt.savefig('iperf_bandwidth.png')
plt.show()