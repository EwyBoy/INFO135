# 17.03.2022 - Laget av Eivind Norling

# Har laget oppgaven som en kjørbar fil.
# Task 1 til 3 kan alle kjøres med denne filen i terminalen.

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 1 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

# Given the following Graph, which set represents the Edge set of the Graph?
    # a) { (A,B), (B,C), (B,D), (C,A), (C,D) }
    # b) { (A,B), (B,C), (B,D), (C,A), (D,A) }
    # c) { (A,B), (B,C), (C,B), (C,A), (D,A) }
    # d) { (A,B), (B,C), (A,C), (C,A), (D,B) }
    # e) None of the above 

# Answer: B

def task_1():
    print('Answer: B')
    main()

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 2 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

# N-Queens Problem

COLUMNS = 'abcde'
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []

def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)

    return results

def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE

def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    return (
        row1 == row2 or
        column1 == column2 or
        abs(row1-row2) == abs(column1-column2)
    )

def solve(partial_sol):
    exam = examine(partial_sol)
    if exam == ACCEPT:
        print(partial_sol)
    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)            

def is_solution(candidate_solution):
    if len(candidate_solution) == NUM_QUEENS:
        if examine(candidate_solution) == ACCEPT:
            all_solutions.append(candidate_solution)
            return 'Valid solution!'
    return 'Invalid solution!'


def task_2():
    candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
    candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']

    result1 = is_solution(candidate_solution1)
    result2 = is_solution(candidate_solution2)
    
    print("Candidate Solution 1:", result1)
    print("Candidate Solution 2:", result2)
    
    main()


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 3 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------    

class Graph():

    def __init__(self):
        self.visited = set()
        self.graph = dict()

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = [node2]
        else:
            self.graph[node1].append(node2)

    def print_graph(self):
        print(self.graph)

    def find_cycle(self, node):
        # if node is not in graph, return false
        if node in self.graph:
            # if node is in visited, return true
            for neighbour in self.graph[node]:
                # if neighbour is in visited, return true
                if neighbour in self.visited:
                    return 'Cycle found!'
                # if neighbour is not in visited, add neighbour to visited and call find_cycle on neighbour
                self.visited.add(neighbour)
                # use recursion to find cycle in neighbour
                if self.find_cycle(neighbour):
                    return 'Cycle found!'          
        return 'Cycle not found!'

def task_3():
    my_graph = Graph()

    my_graph.add_edge('A', 'B')
    my_graph.add_edge('B', 'D')
    my_graph.add_edge('C', 'B')
    my_graph.add_edge('C', 'J')
    my_graph.add_edge('D', 'E')
    my_graph.add_edge('D', 'F')
    my_graph.add_edge('E', 'C')
    my_graph.add_edge('E', 'G')
    my_graph.add_edge('F', 'H')
    my_graph.add_edge('G', 'I')

    result = my_graph.find_cycle('A')
    print(result)

    main()

# -------------------------------------------------------------------------------------------------------------------------------

# Runnable launcher
def main():
    print('\nAvaliable runnable tasks:\n' + '1 :: Task 1' + '\n' + '2 :: Task 2' + '\n' + '3 :: Task 3' + '\n' + 'x :: Exit')

    task = str(input("Input the number of the task you want to run: "))
    print('\n')

    if task == '1':
        task_1()
    elif task == '2':
        task_2()
    elif task == '3':
        task_3()
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