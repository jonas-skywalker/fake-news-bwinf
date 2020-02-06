class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def create_graph(file):
        edges = parse_nodes(file)
        nodes_dict = dict()
        for (v, u) in edges:
            if v not in nodes_dict:
                nodes_dict[v] = []
            if u not in nodes_dict:
                nodes_dict[u] = []
            nodes_dict[v].append(u)
            nodes_dict[u].append(v)
        return Graph(nodes_dict)

    def neighbours(self, v):
        return self.nodes[v]

    def is_neighbour(self, v, u):
        return u in self.neighbours(v)

    def ensure(self, *vs):
        for v in vs:
            if v not in self.nodes:
                self.nodes[v] = []

    def add_edge(self, edge):
        (u, v) = edge
        self.ensure(u, v)
        self.nodes[v].append(u)
        self.nodes[u].append(v)

def parse_nodes(file):
    with open(file, "r") as infile:
        input = infile.readlines()
        head = input[0].split()
        n = head[2]
        m = head[3]

        values = input[1:]
        nodes = list()

        for line in values:
            line_list = line.split()
            nodes.append(tuple(map(int, line_list)))
    return nodes