import re
import sys
import collections
import matplotlib.pyplot as plt
import squarify
import csv

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py log_file.log")
        sys.exit(1)

    input_file = sys.argv[1]
    csv_output_file = "output.csv"
    plot_output_file = input_file.split(".")[0] + ".png"

    logs = []
    with open(input_file, 'r') as log_file:
        for line in log_file:
            match = re.search(r':(.*?):.*?:(.*?):', line)
            if match:
                logs.append(match.group(2).strip())

    count = dict(collections.Counter(logs))

    with open(csv_output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Field", "Count"])
        for key, value in count.items():
            writer.writerow([key, value])

    labels = list(count.keys())
    values = list(count.values())
    plt.figure(figsize=(15, 8))
    squarify.plot(sizes=values, label=labels, alpha=.8 )
    plt.axis('off')
    plt.savefig(plot_output_file)

