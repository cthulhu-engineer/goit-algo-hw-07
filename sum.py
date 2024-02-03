from test_tree import create_test_tree


def find_sum(root):
    if root is None:
        return 0
    return root.value + find_sum(root.left) + find_sum(root.right)


if __name__ == '__main__':
    tree = create_test_tree()
    print(find_sum(tree))
