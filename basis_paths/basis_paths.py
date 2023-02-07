import networkx as nx
import csv

def mccabe_basis_path(graph, entry_node, exit_node):
    def dfs_paths(graph, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if node not in path:
                new_paths = dfs_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    control_flow_graph = nx.DiGraph()

    # Add nodes to the control flow graph
    for node in graph:
        control_flow_graph.add_node(node)

    # Add edges to the control flow graph
    for node in graph:
        for successor in graph[node]:
            control_flow_graph.add_edge(node, successor)

    # Find all paths in the control flow graph
    all_paths = dfs_paths(control_flow_graph, entry_node, exit_node)

    # Calculate the McCabe's Basis Path
    mccabe_basis_path = len(all_paths)

    return all_paths

# Prompt the user to enter the input file
input_file = input("Enter the name of the input file: ")

# Read the input file
graph = {}
with open(input_file) as file:
    reader = csv.reader(file)
    for row in reader:
        node1, node2 = row
        if node1 in graph:
            graph[node1].append(node2)
        else:
            graph[node1] = [node2]

# Prompt the user to enter the entry and exit nodes
entry_node = input("Enter the entry node: ")
exit_node = input("Enter the exit node: ")

# Calculate the McCabe's Basis Path
all_paths = mccabe_basis_path(graph, entry_node, exit_node)

# Prompt the user to enter the output file
output_file = input("Enter the name of the output file: ")

# Write the output to the file
with open(output_file, "w", newline='') as file:
    writer = csv.writer(file)
    for path in all_paths:
        writer.writerow(path)

# Output the number of nodes, edges, and McCabe basis paths to the command line
print("Number of nodes: ", len(graph))
print("Number of edges: ", sum(len(v) for v in graph.values()))
print("Number of McCabe basis paths: ", len(all_paths))
