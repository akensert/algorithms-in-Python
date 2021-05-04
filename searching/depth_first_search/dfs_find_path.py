from collections import defaultdict
from typing import Dict, DefaultDict, Optional


def dfs_iterative(graph: Dict[int, list],
                  node_orig: int,
                  node_dest: int,
                  visited: DefaultDict[int, bool],
                 ) -> list:
    """
    Iterative depth-first search to find a path from node_orig to node_dest
    """

    stack = [(node_orig, [node_orig])]
    path = []

    while len(stack) > 0:
        node, path = stack.pop()
        if not visited[node]:
            if node == node_dest:
                return path
            visited[node] = True
            for node_adj in graph[node]:
                stack.append((node_adj, path+[node_adj]))

def dfs_recursive(graph: Dict[int, list],
                  node_curr: int,
                  node_dest: int,
                  visited: DefaultDict[int, bool],
                  path: Optional[list] = None
                 ) -> list:
    """
    Recursive depth-first search to find a path from initial node_curr to node_dest
    """

    # if node_curr is starting node, initialize path
    if path is None: path = [node_curr]

    for node_adj in graph[node_curr]:

        if not visited[node_adj]:
            visited[node_adj] = True
            path = dfs_recursive(
                graph, node_adj, node_dest,
                visited, path + [node_adj]
            )

        if path[-1] == node_dest:
            return path

    return path[:-1]

if __name__ == '__main__':
    graph = {1: [2],
             2: [3, 4, 5],
             3: [6],
             4: [5, 7],
             5: [2, 6, 7],
             6: [3, 8],
             7: [8, 11],
             8: [7],
             9: [7],
             10: [7, 9],
             11: [10, 12],
             12: [13],
             13: [11]}

    print("Graph: ")
    for k, v in graph.items():
        print("{:>2d} : {}".format(k, v))
    print('--'*20)

    print("Iterative DFS:")
    print("Path from 1 to 13")
    print(dfs_iterative(graph, 1, 13, defaultdict(bool)))
    print('--'*20)

    print("Recursive DFS:")
    print("Path from 1 to 13")
    print(dfs_recursive(graph, 1, 13, defaultdict(bool)))
    print('--'*20)
