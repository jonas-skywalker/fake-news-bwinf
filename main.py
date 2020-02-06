class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def neighbours(self, v):
        return self.nodes[v]

    def ensure(self, *vs):
        for v in vs:
            if v not in self.nodes:
                self.nodes[v] = []

    def add_edge(self, edge):
        (u, v) = edge
        self.ensure(u, v)
        self.nodes[v].append(u)
        self.nodes[u].append(v)

def create_graph(edges):
    nodes_dict = dict()
    for (v, u) in edges:
        if v not in nodes_dict:
            nodes_dict[v] = []
        if u not in nodes_dict:
            nodes_dict[u] = []
        nodes_dict[v].append(u)
        nodes_dict[u].append(v)
    return Graph(nodes_dict)

print(create_graph([(1,2), (2,3), (6,3)]).nodes)

infile = "23432 543435\n432423 543"
ret = []
for i in infile.split('\n'):
    parts = i.split()
    ret.append(tuple(map(int, parts)))
print(ret)