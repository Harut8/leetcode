graph = {
    0: [1],
    1: [2],
    2: [],
    3: [4],
    4: [5],
    5: [3]
}


def has_cycle(graph):
    visited = set()
    stack = set()
    def dfs(node):
        visited.add(node)
        stack.add(node)
        for child in graph[node]:
            if child not in visited:
                if dfs(child):
                    return True
            elif child in stack:
                return True
        stack.remove(node)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


print(has_cycle(graph))