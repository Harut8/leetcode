from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(start, end):
    visited = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)
    return False

print(bfs('A', 'F'))