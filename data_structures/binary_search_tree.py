from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    key: Optional[int]
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    parent: Optional['Node'] = None


class BinarySearchTree:

    def __init__(self, array: List[int]) -> None:
        self.root = None
        for a in array:
            self.root = self.insert(self.root, a)

    def insert(self, node: Node, key: int) -> Node:

        if node is None:
            return Node(key)

        if key <= node.key:
            node.left = self.insert(node.left, key)
            node.left.parent = node
        else:
            node.right = self.insert(node.right, key)
            node.right.parent = node

        return node

    def traverse(self, root: Node, data: Optional[List[int]] = None) -> List[int]:
        """traverse tree from in an ascending order"""
        if root is not None:
            if root.parent is None:
                data = []
            data = self.traverse(root.left, data)
            data.append(root.key)
            data = self.traverse(root.right, data)
        return data


if __name__ == '__main__':

    array = [9, 11, 13, 4, 4, 8, 9, 4, 12]
    print("original array:", array)
    bst = BinarySearchTree(array)
    print("tree traverse: ", bst.traverse(bst.root))
