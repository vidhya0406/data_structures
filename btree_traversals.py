class BinaryTree:
    def __init__(self, root_node):
        self.left_node = None
        self.right_node = None
        self.root = root_node

    def get_left_child(self):
        return self.left_node

    def get_right_child(self):
        return self.right_node

    def set_node_value(self,value):
        self.root = value

    def get_node_value(self):
        return self.root

    def insert_right(self, node):

        if self.right_node is None:
            self.right_node = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.right_node = self.right_node
            self.right_node = temp

    def insert_left(self, node):

        if self.left_node is None:
            self.left_node = BinaryTree(node)
        else:
            temp = BinaryTree(node)
            temp.left_node = self.left_node
            self.left_node = temp

    def in_order_print(self, root=None):
        if root:
            self.in_order_print(root.get_left_child)
            print(root.getNodeValue())
            self.in_order_print(root.getRightChild())
        else:
            self.in_order_print(self.root.get_left_child)
            print(self.root.getNodeValue())
            self.in_order_print(self.root.getRightChild())

    def pre_order_print(self, root=None):
        if root:
            print(root.getNodeValue())
            self.pre_order_print(root.get_left_child)
            self.pre_order_print(root.getRightChild())
        else:
            print(self.root.getNodeValue())
            self.pre_order_print(self.root.get_left_child)
            self.pre_order_print(self.root.getRightChild())

    def post_order_print(self, root=None):
        if root:
            self.post_order_print(root.get_left_child)
            self.post_order_print(root.getRightChild())
            print(root.getNodeValue())
        else:
            self.post_order_print(self.root.get_left_child)
            self.post_order_print(self.root.getRightChild())
            print(self.root.getNodeValue())
