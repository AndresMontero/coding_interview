class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return []

        total_paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    total_paths.append(p)

        return total_paths

    def get_shortest_path(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                tmp_sp = self.get_shortest_path(node, end, path)
                if tmp_sp:
                    if shortest_path is None or len(tmp_sp) < len(shortest_path):
                        shortest_path = tmp_sp
        return shortest_path


if __name__ == '__main__':
    routes = [
        ('cochabamba', 'santa_cruz'),
        ('santa_cruz', 'la_paz'),
        ('cochabamba', 'tarija'),
        ('tarija', 'beni'),
        ('beni', 'santa_cruz'),
        ('cochabamba', 'pando'),
        ('oruro', 'potosi'),
        ('oruro', 'santa_cruz'),
        ('potosi', 'cochabamba'),
    ]

    start = 'potosi'
    end = 'la_paz'

    route_graph = Graph(routes)
    print(route_graph.graph_dict)
    print(f"Paths between {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))
