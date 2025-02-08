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
        if self.length == 0:
            return
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next =  self.head
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def incert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True 

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst(value)
        if index == self.length:
            return self.pop(value)
        pre_temp = self.get(index -1 )
        temp = self.get(index)
        pre_temp.next = temp.next

    def reverse(self):
        self.head

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

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
my_linklist.set(0,9)
print("\n")
my_linklist.printList()
my_linklist.incert(2,9898)
print("\n")
my_linklist.printList()
my_linklist.remove(2)
print("\n")
my_linklist.printList()