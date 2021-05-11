from collections import defaultdict


class Dijkstra:
    """
    Dijkstra shortest path finder given a graph, starting node and ending node.
    Does not implement efficient min extraction ('extract-min').
    Todo: implement a heap for min extraction.
    """
    def __init__(self, graph):
        self.G = graph
        self.Q = defaultdict(lambda: float('inf'))

    def extract_min(self):
        minval = float('inf')
        for k, v in self.Q.items():
            if v < minval:
                minval = v
                argmin = k
        del self.Q[argmin]
        return (argmin, minval)

    def find_shortest_path(self, node_orig, node_dest):
        """
        v_d:  distance between v and node_orig
        w_d:  distance between v and w
        vw_d: distance between node_orig and w
              (is updated when a shorter path is found)
        """
        self.Q[node_orig] = 0
        self.S = defaultdict(lambda: None)
        self.P = defaultdict(lambda: [(node_orig, 0)])

        while len(self.Q):
            (v, v_d) = self.extract_min()
            self.S[v] = v_d
            for (w, w_d) in self.G[v]:
                if not self.S[w]:
                    vw_d = v_d + w_d
                    if self.Q[w] > vw_d:
                        self.Q[w] = vw_d
                        self.P[w] = self.P[v] + [(w, w_d)]

        return self.P[node_dest]


if __name__ == '__main__':
    graph = {
        1 : [(2,  3), (4,  4), (13, 7)],
        2 : [(1,  3), (4,  4), (8,  1), (13,  2)],
        3 : [(12, 2), (13, 2)],
        4 : [(1,  4), (2,  4), (6,  5)],
        5 : [(7,  2), (11, 5)],
        6 : [(4,  5), (8,  3)],
        7 : [(8,  2), (5,  2)],
        8 : [(2,  1), (6,  3), (7,  2)],
        9 : [(10, 6), (11, 4), (12, 4)],
        10: [(9,  6), (11, 4), (12, 4)],
        11: [(5,  5), (9,  4), (10, 4)],
        12: [(3,  2), (9,  4), (10, 4)],
        13: [(1,  7), (2,  2), (3,  3)],
    }

    print("---"*20 + "\nGraph:\n" + "---"*20)
    for k, v in graph.items():
        print(k, v)
    print('---'*20)
    dijkstra = Dijkstra(graph)
    shortest_path = dijkstra.find_shortest_path(13, 5)
    print("Shortest path from 13 to 5 =", shortest_path)
