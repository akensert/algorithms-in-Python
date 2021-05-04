from collections import defaultdict
from typing import List, Tuple, DefaultDict


class SCCFinder():
    """
    Kosaraju's two-pass algorithm to find strongly connected components;
    probably not the most concise/efficient Python implementation of the
    Kosaraju algorithm.
    """
    def __init__(self, graph: List[Tuple[int, int]]) -> None:
        """
        Converts List[Tuple[int, int]] graph to DefaultDict[int, List[int]]
        graph, and computes the range of vertices to be looped over (backwards)
        """
        self.graph = defaultdict(list)
        self.graph_rev = defaultdict(list)

        self.V_min = float('inf')
        self.V_max = float('-inf')
        for edge in graph:
            (v, w) = edge
            self.graph[v].append(w)
            self.graph_rev[w].append(v)
            if min(v, w) < self.V_min: self.V_min = min(v, w)
            if max(v, w) > self.V_max: self.V_max = max(v, w)

        self.V = range(self.V_max, self.V_min-1, -1)

    def _dfs_first_pass(self,
                        graph_rev: DefaultDict[int, List[int]],
                        node: int
                       ) -> None:
        """Obtains finishing times of the reversed graph"""
        stack = [node]
        while len(stack):
            # notice no pop of stack, need to label it for finishing time
            node = stack[-1]
            if not self.visited[node]:
                self.visited[node] = True
                for node_adj in graph_rev[node]:
                    stack.append(node_adj)
            else:
                node = stack.pop()
                if not self.finished[node]:
                    self.finished[node] = True
                    self.finishing_time[self.i] = node
                    self.i += 1

    def _dfs_second_pass(self,
                         graph: DefaultDict[int, List[int]],
                         node: int
                        ) -> None:
        """Obtains strongly connected components of graph"""
        stack = [node]
        source_node = stack[-1]
        while len(stack):
            node = stack.pop()
            if not self.visited[node]:
                self.visited[node] = True
                self.scc[source_node].append(node)
                for node_adj in graph[node]:
                    stack.append(node_adj)

    def find_scc(self) -> DefaultDict[int, List[int]]:

        # first pass
        self.i = self.V_min # number of nodes processed so far
        self.finishing_time = defaultdict(bool)
        self.visited = defaultdict(bool)
        self.finished = defaultdict(bool)
        for v in self.V:
            if not self.visited[v]:
                self._dfs_first_pass(self.graph_rev, v)

        # second pass
        self.visited = defaultdict(bool)
        self.scc = defaultdict(list)
        for v in self.V:
            v = self.finishing_time[v]
            if not self.visited[v]:
                self._dfs_second_pass(self.graph, v)

        return self.scc

if __name__ == "__main__":
    graph = [
        (1, 2),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 6),
        (4, 5),
        (4, 7),
        (5, 2),
        (5, 6),
        (5, 7),
        (6, 3),
        (6, 8),
        (7, 8),
        (7, 11),
        (8, 7),
        (9, 7),
        (10, 7),
        (10, 9),
        (11, 10),
        (11, 12),
        (12, 13),
        (13, 11),
    ]

    scc_finder = SCCFinder(graph)

    print("Graph: ")
    for k, v in scc_finder.graph.items():
        print("{:>2d} : {}".format(k, v))
    print('--'*20)

    scc = scc_finder.find_scc()
    print("SCCs:")
    for k, v in scc.items():
        print(k, v)
