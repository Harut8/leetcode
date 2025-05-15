graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


visited = set()
def dfs(start, end):
    if start == end:
        return True
    for child in graph[start]:
        if child not in visited:
            visited.add(start)
            if dfs(child, end):
                return True
    return False

print(dfs('A', 'F'))