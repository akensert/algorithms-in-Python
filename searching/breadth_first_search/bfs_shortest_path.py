from collections import defaultdict
from typing import Dict, List, Union

def bfs_paths(graph: Dict[int, List[int]],
              node_orig: int) -> None:
    visited = defaultdict(bool)
    Q = [(node_orig, [])]
    while len(Q):
        v, path = Q.pop(0)
        path.append(v)
        print(f">> Path from {node_orig:<2d} to {v:>2d}: {path}")
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                Q.append((w, path[:]))
    return None

def bfs_path(graph: Dict[int, List[int]],
             node_orig: int,
             node_dest: int) -> Union[List[int], None]:
    visited = defaultdict(bool)
    Q = [(node_orig, [])]
    while len(Q):
        v, path = Q.pop(0)
        path.append(v)
        if path[-1] == node_dest:
            return path
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                Q.append((w, path[:]))
    return None


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

    node_orig = 1
    node_dest = 10

    print(f"bfs_paths(graph, {node_orig})")
    _ = bfs_paths(graph, node_orig)
    print('--'*30)

    print(f"bfs_path(graph, {node_orig}, {node_dest})")
    shortest_path = bfs_path(graph, node_orig, node_dest)

    if shortest_path:
        print(f">> Path from {node_orig:<2d} to {node_dest:>2d}:",
              shortest_path)
    else:
        print(f">> No path found from {node_orig} to {node_dest}")
