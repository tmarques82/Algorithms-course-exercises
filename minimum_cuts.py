"""
Script for computing the minimum cuts problem in a graph given by a file
"""

from random import randint
from math import log


def parse_file(file_to_parse):
    with open(file_to_parse, 'r') as f:
        a = f.readlines()
        def parse_line(x):
            elems = x.split('\t')
            outp = []
            for elem in elems:
                if elem.isdigit():
                    outp.append(int(elem))
            return outp

        return [parse_line(x) for x in a]


def process_graph_matrix(graph_matrix):
    vertices = {}
    edges = {}
    edge_number = 1
    for inp in graph_matrix:
        vertex = inp[0]
        for i in range(1, len(inp)):
            second_vertex = inp[i]
            if second_vertex > vertex:
                #only compute one direction
                edges[edge_number] = [vertex, second_vertex]
                if not vertices.get(vertex):
                    vertices[vertex] = set([])
                vertices[vertex].add(edge_number)
                if not vertices.get(second_vertex):
                    vertices[second_vertex] = set([])
                vertices[second_vertex].add(edge_number)
                edge_number += 1
    return vertices, edges


def get_min_cuts(graph_matrix):
    verts, edges = process_graph_matrix(graph_matrix)
    last_vert_number = len(verts) + 1

    while len(verts) > 2:
        edges_keys = list(edges.keys())
        random_index = randint(0, len(edges) - 1)
        random_edge = edges_keys[random_index]

        affected_vertices = edges[random_edge]
        edges_first_vertex = verts.pop(affected_vertices[0])
        edges_second_vertex = verts.pop(affected_vertices[1])
        edges_to_remove = edges_first_vertex.intersection(edges_second_vertex)
        resulting_vertices_edges = edges_first_vertex.union(edges_second_vertex)
        resulting_vertices_edges = resulting_vertices_edges.difference(edges_to_remove)
        for edge_to_remove in edges_to_remove:
            edges.pop(edge_to_remove)
        verts[last_vert_number] = resulting_vertices_edges
        for edge_index in resulting_vertices_edges:
            for i in (0, 1):
                if edges[edge_index][i] in affected_vertices:
                    edges[edge_index][i] = last_vert_number
        last_vert_number += 1
    min_cuts = len(edges)
    return min_cuts


def get_min_iterations(numvertex):
    """
    Compute the number of runnings for ensuring the result in a high percentage
    """
    return round(numvertex*numvertex*log(numvertex)) + 1



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a file with graph, in format u->v per line')
    parser.add_argument('--f', dest='file_to_parse',
        help='File to parse')

    args = parser.parse_args()

    graph_matrix = parse_file(args.file_to_parse)

    min_cuts = get_min_cuts(graph_matrix)
    iterations = get_min_iterations(len(a))

    print('Number of iterations: {0}'.format(iterations))

    for i in range(iterations):
        min_cuts_prov = get_min_cuts(graph_matrix)
        if min_cuts_prov < min_cuts:
            print ('NEW MIN CUTS....')
            print(min_cuts_prov)
            min_cuts = min_cuts_prov


    print ('AND THE FINAL RESULT IS....')
    print(min_cuts)
