import csv
import sys
import getopt

def calculate_paths(edges, vertices, start, end):
    paths = [[start]]
    while paths:
        path = paths.pop()
        vertex = path[-1]
        if vertex == end:
            yield path
        else:
            for neighbor in vertices:
                if (vertex, neighbor) in edges and neighbor not in path:
                    paths.append(path + [neighbor])




def main(argv):
    #input_file = 'graph.csv'
    output_file = None

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('bfs_search.py -i <inputfile> -o <outputfile> <start> <end>')
        print('OR')
        print('bfs_search.py -i <inputfile> <start> <end>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('bfs_search.py -i <inputfile> -o <outputfile> <start> <end>')
            print('OR')
            print('bfs_search.py -i <inputfile> <start> <end>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    if len(args) != 2:
        print('bfs_search.py -i <inputfile> -o <outputfile> <start> <end>')
        print('OR')
        print('bfs_search.py -i <inputfile> <start> <end>')
        sys.exit(2)
    start, end = map(int, args[0:2])

    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        edges = [(int(row[0]), int(row[1])) for row in reader]
        vertices = list(set([u for u, v in edges] + [v for u, v in edges]))

    if output_file is None:
        for path in calculate_paths(edges, vertices, start, end):
            print(', '.join(map(str, path)))

    else:
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            for path in calculate_paths(edges, vertices, start, end):
                writer.writerow(path)

if __name__ == "__main__":
    main(sys.argv[1:])
    