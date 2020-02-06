import graph

def tap_network_of_trumpf(gr):
    by_connectivity = ordered_connectivity_list(gr)
    tapped = set()
    while by_connectivity:
        vertex = by_connectivity[0]
        del by_connectivity[0]

        tapped.add(vertex)
        for ((v, neighs), index) in enumerate(by_connectivity):
            if gr.is_neighbour(v, vertex):
                by_connectivity[index] = (v, neighs - 1)

        by_connectivity.sort(key=lambda x: x[1], reversed=True)
    return tapped

def ordered_connectivity_list(graph):
    with_conn = list()
    for vertex in graph.nodes:
        with_conn.append((vertex, len(graph.neighbours(vertex))))
    return sorted(with_conn, key=lambda x: x[1], reverse=True)
