import graph
import algorithm
import time

print("test")
start = time.time()
gr = graph.Graph.create_graph(r".\jugendforumInformatik2020\problem\input\hard_5.graph")
print(len(algorithm.tap_network_of_trumpf(gr)), time.time() - start)
