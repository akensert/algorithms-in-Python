from collections import defaultdict

def dfs(graph, v, visited, labels):
    global i
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited, labels)
    labels[v] = i
    i -= 1

def dfs_loop(graph):
    visited = defaultdict(bool)
    labels = {}
    for v in graph.keys():
        if not visited[v]:
            dfs(graph, v, visited, labels)
    return labels


if __name__ == '__main__':
    graph = {1: [2, 3, 4, 5],
             2: [4],
             3: [4, 5],
             4: [5],
             5: []}

    print("Graph:")
    print(graph)
    i = max(graph.keys())

    labels = dfs_loop(graph)
    print("Topology (finishing times):")
    for k, v in labels.items():
        print(f"node {k}, label {v}")
