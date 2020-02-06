import graph
import algorithm
print("test")
gr = graph.Graph.create_graph(r".\jugendforumInformatik2020\problem\input\easy_1.graph")
print(len(algorithm.tap_network_of_trumpf(gr)))