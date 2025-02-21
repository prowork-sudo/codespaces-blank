class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary_search_tree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: return True
        return False

    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        if current_node is None:
            return result
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result
    
    def DFS_preorder(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def DFS_postorder(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result

    def DFS_inorder(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result


my_tree = binary_search_tree()
my_tree.insert(5)
print(my_tree.root.value)
my_tree.insert(1)
print(my_tree.root.left.value)
my_tree.insert(9)
print(my_tree.root.right.value)
print(my_tree.contains(0))
print(my_tree)
my_tree.insert(92)
my_tree.insert(19)
my_tree.insert(23)
my_tree.insert(7)
my_tree.insert(0)
my_tree.insert(4)
my_tree.insert(999)


print(my_tree.BFS())  # this will print the  BFS traversal
print(my_tree.DFS_preorder()) # this will print BFS Preorder traversal
print(my_tree.DFS_postorder()) # this will print BFS Postorder traversal
print(my_tree.DFS_inorder()) # this will print BFS Postorder traversal