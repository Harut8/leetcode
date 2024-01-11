class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(self, root) :
    if not root:
        return []
    ans = []
    queue = []
    queue.append(root)
    while queue:
        cur_lev = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            cur_lev.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(cur_lev)
    return ans


if __name__ == '__main__':
    Node = TreeNode
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(levelOrder(root))
