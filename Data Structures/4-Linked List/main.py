class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """Appends a new node with the given value to the end of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Removes and returns the value of the last node in the list."""
        if self.length == 0:
            return None  # Return None if the list is empty
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value  # Return the value

    def prepend(self, value):
        """Adds a new node with the given value to the beginning of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        """Removes and returns the value of the first node in the list."""
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        """Returns the node at the given index (or None if invalid index)."""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        """Sets the value of the node at the given index."""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):  # Corrected name
        """Inserts a new node with the given value at the given index."""
        if index < 0 or index > self.length: # Corrected condition
            return False # Return False if index is invalid
        if index == 0:
            return self.prepend(value)
        if index == self.length: # Append if index is equal to length
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Removes and returns the value of the node at the given index."""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()

        pre_temp = self.get(index - 1)
        temp = self.get(index)
        pre_temp.next = temp.next
        temp.next = None  # Disconnect the removed node
        self.length -= 1  # Decrement the length
        return temp.value  # Return the value

    def reverse(self):
        """Reverses the linked list in place."""
        before = None
        current = self.head
        self.head, self.tail = self.tail, self.head  # Efficient swap
        for _ in range(self.length):
            next_node = current.next
            current.next = before
            before = current
            current = next_node
        self.tail.next = None  # Set the new tail's next to None

    def printList(self):
        """Prints the values of all nodes in the list."""
        temp = self.head
        while temp:  
            print(temp.value)
            temp = temp.next


# Example usage (no changes needed from your previous example):
my_linklist = LinkedList(4)
my_linklist.append(7)
my_linklist.append(7)
my_linklist.append(6)
my_linklist.append(7)
my_linklist.printList()
print("\n")
my_linklist.pop()
my_linklist.printList()
my_linklist.prepend(5)
print("\n")
my_linklist.printList()
my_linklist.popfirst()
print("\n")
my_linklist.printList()
print("\n")
print(my_linklist.get(0).value)
my_linklist.set(0, 9)
print("\n")
my_linklist.printList()
my_linklist.insert(2, 9898) 
print("\n")
my_linklist.printList()
my_linklist.remove(2)
print("\n")
my_linklist.printList()
my_linklist.reverse()
print("\n")
my_linklist.printList()