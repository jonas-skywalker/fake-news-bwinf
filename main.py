class Graph:
    def __init__(self):
        self.nodes = dict()

    def parse_notes(self, file):
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
