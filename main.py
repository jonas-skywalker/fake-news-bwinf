import graph
import algorithm

gr = graph.Graph.create_graph(r".\jugendforumInformatik2020\problem\input\medium_4.graph")

print(len(algorithm.tap_network_of_trumpf(gr)))