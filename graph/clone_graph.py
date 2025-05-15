# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return self is other

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}
        def clone(_node):
            if _node in visited:
                return visited[_node]
            _cloned = Node(val=_node.val)
            visited[_node] = _cloned
            for ngb in _node.neighbors:
                _cloned.neighbors.append(clone(ngb))
            return _cloned
        return clone(node)
