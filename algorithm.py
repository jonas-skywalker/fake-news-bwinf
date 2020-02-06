def tap_network_of_trumpf(gr):
    connectivities = connectivity_list(gr)
    tapped = set()
    while connectivities:
        (index, (vertex, connectivity)) = max(enumerate(connectivities), key=lambda x: x[1][1])
        if not connectivity:
            break

        del connectivities[index]

        tapped.add(vertex)
        for (index, (v, neighs)) in enumerate(connectivities):
            if gr.is_neighbour(v, vertex):
                connectivities[index] = (v, neighs - 1)

    return tapped

def connectivity_list(graph):
    return list(map(lambda x: (x[0], len(x[1])), graph.node_neighbour_pairs()))
