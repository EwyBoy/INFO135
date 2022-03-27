# 03.27.2022 - Laget av Eivind Norling

# Har laget oppgaven som en kjørbar fil.
# Task 1 til 4 kan alle kjøres med denne filen i terminalen.

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 1 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

class BinaryTree:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node

    def is_compleate_binary_tree(self):
        if self.left is None and self.right is None:
            return True
        elif self.left is None or self.right is None:
            return False
        else:
            return self.left.is_compleate_binary_tree() and self.right.is_compleate_binary_tree()



def build_binary_tree_1():
    node_a = BinaryTree('a')
    node_a.insert_left('b')
    node_a.insert_right('c')

    node_c = node_a.right
    node_c.insert_left('d')
    node_c.insert_right('e')

    node_d = node_c.left
    node_d.insert_left('f')
    node_d.insert_right('g')

    return node_a

def build_binary_tree_2():
    node_a = BinaryTree('a')
    node_a.insert_left('b')
    node_a.insert_right('c')

    node_b = node_a.left
    node_c = node_a.right

    node_b.insert_left('d')
    node_b.insert_right('e')

    node_c.insert_left('f')
    node_c.insert_right('g')

    node_e = node_b.right
    node_g = node_c.right

    node_e.insert_left('h')
    node_e.insert_right('i')

    node_g.insert_left('j')
    node_g.insert_right('k')

    node_h = node_e.left
    node_h.insert_left('l')
    node_h.insert_right('m')

    return node_a


def build_binary_tree_3():
    node_a = BinaryTree('a')
    node_a.insert_left('b')
    node_a.insert_right('c')

    node_c = node_a.right
    node_c.insert_left('d')
    node_c.insert_right('e')
    
    node_e = node_c.right
    node_e.insert_left('f')
    node_e.insert_right('g')

    node_g = node_e.right
    node_g.insert_left('h')
    node_g.insert_right('i')

    return node_a


# They are all compleate binary trees
def task_1():
    tree_1 = build_binary_tree_1()
    print('Is the tree compleate? ', tree_1.is_compleate_binary_tree())
    tree_2 = build_binary_tree_2()
    print('Is the tree compleate? ', tree_2.is_compleate_binary_tree())
    tree_3 = build_binary_tree_3()
    print('Is the tree compleate? ', tree_3.is_compleate_binary_tree())

    main()

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 2 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


def binary_tree(r):
    return [r, [], []]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def insert_left_child(root, new_node):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_node, t, []])
    else:
        root.insert(1, [new_node, [], []])
    return root        

def insert_right_child(root, new_node):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_node, [], t])
    else:
        root.insert(2, [new_node, [], []])
    return root

def make_tree():
    r = binary_tree('1')
    insert_left_child(r, '2')
    insert_right_child(r, '3')
    insert_left_child(get_left_child(r), '4')
    insert_right_child(get_left_child(r), '5')
    insert_right_child(get_right_child(r), '6')

    return print(r)

def task_2():
    make_tree()
    main()


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 3 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------    

class Graph:
    graph = dict()
    searched = []

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def breadth_first_search(self, node):
        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)
            print('[', node, end=' ], ')
            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour) 

    def depth_first_search(self, node):
        if node not in self.searched:
            print('[', node, end=' ], ')
            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)

    def print_edges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print(node, '->', neighbour)        

    def print_graph(self):
        print(self.graph)        


def build_my_graph():
    my_graph = Graph()

    my_graph.add_edge('A', 'B')
    my_graph.add_edge('A', 'C')
    my_graph.add_edge('B', 'C')
    my_graph.add_edge('B', 'D')
    my_graph.add_edge('C', 'E')
    my_graph.add_edge('D', 'E')
    my_graph.add_edge('E', 'F')
    my_graph.add_edge('F', 'C')
    my_graph.add_edge('D', 'G')
    my_graph.add_edge('D', 'H')

    return my_graph

def task_3():

    my_graph = build_my_graph()
    print('Edges:\n')
    my_graph.print_edges()
    print('\nBFS:\n')
    my_graph.breadth_first_search('A')
    print('\n\nDFS:\n')
    my_graph.depth_first_search('A')
    print('\n')

    main()

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 4 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------    

class BinarySearchTree:

    def __init__(self, value=None):
        self.value = value
        if (self.value):
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else:
            self.left = None
            self.right = None    

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        elif value < self.value:
            self.left.insert(value)
        elif value > self.value:
            self.right.insert(value)        

    def in_order(self):
        if not self.is_empty():
            self.left.in_order()
            print(self.value, end=' ')
            self.right.in_order()

    def compute_sum(self):
        if self.is_empty():
            return 0
        else:
            return self.value + self.left.compute_sum() + self.right.compute_sum()

    def compute_count(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.left.compute_count() + self.right.compute_count()                

    def print_tree(self):
        print('Tree: ', end='')
        print(self.in_order())        


def build_my_tree():
    my_tree = BinarySearchTree()

    my_tree.insert(2)
    my_tree.insert(4)
    my_tree.insert(6)
    my_tree.insert(8)
    my_tree.insert(10)

    return my_tree        

def task_4():
    my_tree = build_my_tree()
    print('Sum: ', my_tree.compute_sum())
    print('Count: ', my_tree.compute_count())
    main()    


# -------------------------------------------------------------------------------------------------------------------------------

# Runnable launcher
def main():
    print('\nAvaliable runnable tasks:\n' + '1 :: Task 1' + '\n' + '2 :: Task 2' + '\n' + '3 :: Task 3' + '\n' + '4 :: Task 4' + '\n' + 'x :: Exit')

    task = str(input("Input the number of the task you want to run: "))
    print('\n')

    if task == '1':
        task_1()
    elif task == '2':
        task_2()
    elif task == '3':
        task_3()
    elif task == '4':
        task_4()    
    elif task == 'x':
        exit()
    else:
        invalid_task()         
    print('\n')
       
# Error message for invalid task       
def invalid_task():
    print("Invalid task number. Please try again.")
    main()

# Python looks for this function when it runs the file
if __name__ == "__main__":
    main()

# -------------------------------------------------------------------------------------------------------------------------------