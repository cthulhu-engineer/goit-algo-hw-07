from test_tree import TreeNode, create_test_tree


def find_max(root: TreeNode):
    while root.right:
        root = root.right
    return root.value


if __name__ == '__main__':
    tree = create_test_tree()
    print(find_max(tree))
