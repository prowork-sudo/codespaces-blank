class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node 
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None 
            temp.next = None
        self.length -= 1
        return temp
    
# try parallel compute for get and set 


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    

my_doubly_linked_list = DoublyLinkedList(9089)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(8)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(999)
my_doubly_linked_list.prepend(992349)
my_doubly_linked_list.pop_first()
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()
