graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1, 4],
    4: [3]
}


def has_cycle(graph):
    visited = set()
    def dfs(node, parent):
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                dfs(child, node)
            elif child != parent:
                return True
        return False
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

print(has_cycle(graph))