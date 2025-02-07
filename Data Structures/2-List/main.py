my_list = [1, 2, 3, 4, 5, 3]
my_list.append(6)   # add element at the end O(1)
print(my_list)
my_list.remove(1) # remove the first occurance of the element O(n)
print(my_list)
my_list.pop() # remove the last element O(1)
print(my_list)
my_list.pop(0) # remove the first element O(n)
print(my_list)
my_list.insert(0, 0) # (index, value)insert at the requried inex O(n)
print(my_list)
my_list.reverse() # reverse the list O(n)
my_list.sort() # sort the list O(nlogn) 
print(my_list)
