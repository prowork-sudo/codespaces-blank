class graph():
    def __init__(self):
        self.adj_list = {}

    def print_vertex(self):
        for v in self.adj_list:
            print(v, ":", self.adj_list[v])
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False


    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for edge in self.adj_list[vertex]:
                self.adj_list[edge].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

my_graph = graph()
my_graph.add_vertex('a')
my_graph.add_vertex('b')
my_graph.add_vertex('c')
my_graph.add_vertex('d')
my_graph.add_edge('a','b')
my_graph.add_edge('c','d')
my_graph.add_edge('b','d')
my_graph.add_edge('a','d')
#my_graph.remove_edge('a','b')
my_graph.remove_vertex('d')
my_graph.print_vertex()