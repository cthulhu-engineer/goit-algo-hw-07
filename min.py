from test_tree import create_test_tree


def find_min(root):
    while root.left:
        root = root.left
    return root.value


if __name__ == '__main__':
    tree = create_test_tree()
    print(find_min(tree))