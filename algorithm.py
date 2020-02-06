def tap_network_of_trumpf(gr):
    by_connectivity = ordered_connectivity_list(gr)
    tapped = set()
    while by_connectivity:
        (vertex, connectivity) = by_connectivity[0]
        if not connectivity:
            break

        del by_connectivity[0]

        tapped.add(vertex)
        for (index, (v, neighs)) in enumerate(by_connectivity):
            if gr.is_neighbour(v, vertex):
                by_connectivity[index] = (v, neighs - 1)

        by_connectivity.sort(key=lambda x: x[1], reverse=True)
    return tapped

def ordered_connectivity_list(graph):
    with_conn = list()
    for vertex, neighs in graph.node_neighbour_pairs():
        with_conn.append((vertex, len(neighs)))
    return sorted(with_conn, key=lambda x: x[1], reverse=True)
