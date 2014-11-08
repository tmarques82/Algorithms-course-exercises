"""
Script for getting from a file of vertices the 5 biggest sizes of SCCs (Strong Connected Components).
The format file should be a group of lines having the first vertex and the second of every edge separated
by spaces in each line.
"""
import sys
import argparse


def parse_file(file_to_parse):
    """
    Parses the file and returns the graph dictionary, the reversed graph and the last node
    """
    g = {}
    g_reversed = {}
    last_node = 0

    with open(args.file_to_parse, 'r') as f:
        a = f.readlines()
        def parse_line(x):
            elems = x.split(' ')
            key = long(elems[0])
            value = long(elems[1])
            if key not in g:
                g[key] = []
            g[key].append(value)
            if value not in g_reversed:
                g_reversed[value] = []
            g_reversed[value].append(key)
            return max (key, value)

        for x in a:
            key = parse_line(x)
            last_node = max(key, last_node)
    return g, g_reversed, last_node


def dfs_loop(G, num_nodes_total, order={}):
    """
    Calculates the DFS for both steps in Kosaraju alorithm, so it returns a tuple with order in execution
    (calculates in step 1 to be used in step 2) and the final result, which is useful in step 2
    """
    explored = {}
    leaders = {}
    s = None
    t = long(0)
    sccs = [0,0,0,0,0]

    def dfs(G, i, t):
        explored[i] = True
        leaders[s].append(i)
        for final_node in G.get(i, []):
            if not explored.get(final_node):
                t = dfs(G, final_node, t)
        t += 1
        order[t] = i
        return t

    for i in range(num_nodes_total, 1, -1):
        i = order.get(i, i)
        if not explored.get(i):
            s = i
            leaders[s] = []

            t = dfs(G, i, t)

            num_nodes_in_scc = len(leaders[s])
            min_current_scc = min(sccs)
            if num_nodes_in_scc >  min_current_scc:
                sccs.remove(min_current_scc)
                sccs.append(num_nodes_in_scc)
    sccs.sort(reverse=True)
    return order, sccs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a file with graph, in format u->v per line')
    parser.add_argument('--f', dest='file_to_parse',
        help='File to parse')

    args = parser.parse_args()


    g, g_reversed, last_node = parse_file(args.file_to_parse)

    # Use a bigger recursion limit for big data (new system ulimit would also have to be applied)
    recursion_limit = max(sys.getrecursionlimit(), last_node)
    sys.setrecursionlimit(recursion_limit)

    # DFS of reversed graph, as stated in Kosaraju algorithm
    order, sccs = dfs_loop(g_reversed, last_node)

    # DFS with order set in previous step
    order, sccs = dfs_loop(g, last_node, order=order)

    print 'The five biggest SCCs for the dataset have the following size: {0}'.format(sccs)
