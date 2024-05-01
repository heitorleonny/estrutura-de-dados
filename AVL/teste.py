from Arvore import ArvoreAVL


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


tree = ArvoreAVL()
values = [9, 5, 10, 0, 6, 11, -1, 1, 2]
print("Inserindo valores na árvore:")
for value in values:
    tree.root = ArvoreAVL.insert(tree.root, value)
    print(f"Inserido: {value}")
    print_tree(tree.root)
    print()

# Deletando alguns valores
values_to_delete = [10, 5, 2]
print("Deletando valores da árvore:")
for value in values_to_delete:
    tree.root = ArvoreAVL.delete(tree.root, value)
    print(f"Deletado: {value}")
    print_tree(tree.root)
    print()