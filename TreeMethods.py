    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self, node):
        if not node:
            return ''
        return f'{self._inorder(node.left)} {node.value} {self._inorder(node.right)}'

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if not node:
            return ''
        return f'{node.value} {self._preorder(node.left)} {self._preorder(node.right)}'

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if not node:
            return ''
        return f'{self._postorder(node.left)} {self._postorder(node.right)} {node.value}'

    tree = BinarySearchTree()
nums = [65, 6, 42, 76, 15, 56, 5, 7, 8, 57]
for x in nums:
    tree.insert(x)
    
print(tree.preorder())
print(tree.inorder())
print(tree.postorder())
