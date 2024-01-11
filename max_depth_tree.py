def maxDepth(self, root) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# OR USE BFS AND DO LEVEL ORDER
