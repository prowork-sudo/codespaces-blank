#good to have prime number
class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i , value in enumerate(self.data_map):
            print(i, ":", value)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        while index:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def key(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    
my_hast_table = HashTable()
my_hast_table.set_item('hey', 1500)
my_hast_table.set_item('bay', 150)
my_hast_table.set_item('cay', 1600)
my_hast_table.set_item('day', 100)
my_hast_table.set_item('may', 1505)
print(my_hast_table.get_item('cay'))
print(my_hast_table.key())
my_hast_table.print_table()


        