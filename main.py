import graph
import algorithm
import time

outdirectory = r".\output"
gr = graph.Graph.create_graph(r".\jugendforumInformatik2020\problem\input\hard_1.graph")
for i in range(1, 6):
    for prefix in ["easy", "medium", "hard"]:
        file_name = r".\jugendforumInformatik2020\problem\input" + "\\" + prefix + "_" + str(i) + ".graph"
        gr = graph.Graph.create_graph(file_name)
        tapped = list(algorithm.tap_network_of_trumpf(gr))
        length = len(tapped)
        filecontent = str(length) + "\n"
        for node in tapped:
            filecontent += str(node) + " "
        filecontent = filecontent[:-1]
        with open(outdirectory + "\\" + prefix + "_" + str(i) + ".sol", "w") as outfile:
            outfile.write(filecontent)