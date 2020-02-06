def tap_network_of_trumpf(graph):
    by_connectivity = ordered_connectivity_list(graph)

def ordered_connectivity_list(graph):
    with_conn = list()
    for vertex in graph.nodes:
        with_conn.append((vertex, len(graph.neighbours(vertex))))
    return sorted(with_conn, key=lambda x: x[1], reverse=True)

