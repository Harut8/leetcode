def is_symmetric(root):
    def symmetric(left, right):
        if not left or not right:
            return left == right

        return left.val == right.val and symmetric(left.left, right.right) and symmetric(right.right, left.left)

    return symmetric(root, root)
