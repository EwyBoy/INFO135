# 28.01.2022 - Laget av Eivind Norling

# Har laget oppgaven som en kjørbar fil.
# Task 1 til 4 kan alle kjøres med denne filen i terminalen.
# Krever python 3.10 pga switch statement.


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 1 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


# Her er svarene til Task 1 i tilfelle du ikke får kjørt oppgaven i terminalen.
# Svarene er rundet opp siden det ikke er mulig å ha 17.3876471435 steps i et binary search.

# Persian dictionary with 171476 words takes 18 steps to find a word in a worst case senario.
# English dictionary with 1100373 words takes 21 steps to find a word in a worst case senario.
# Chinese dictionary with 260000 words takes 18 steps to find a word in a worst case senario.

import math


class Dictionary:
    def __init__(self, language, words):
        self.language = language
        self.words = words

    def calculate_steps(self):
        return math.ceil(math.log2(self.words))

    def find_steps_in_binary_search(self):
        print(f"{self.language} dictionary with {self.words} words takes {self.calculate_steps()} steps to find a word in a worst case senario.")


def task_1():
    Dictionary("Persian", 171476).find_steps_in_binary_search()
    Dictionary("English", 1100373).find_steps_in_binary_search()
    Dictionary("Chinese", 260000).find_steps_in_binary_search()
    main()


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 2 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


class Student:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def greeting(self):
        print(
            f"Hei! my name is {self.name}\nI am {self.age} years old.\nI am from {self.country}.")


def task_2():
    Student("Sara", 25, "Norway").greeting()
    main()


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 3 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def test_linked_list():
 # Create a linked pre_order_traversial_list object
    linked_list = LinkedList()
    # Create a head node object
    linked_list.head = Node('First')
    # Create couple more nodes
    second = Node('Second')
    third = Node('Third')
    # Link first node to second node
    linked_list.head.next = second
    # Link second node to third node
    second.next = third
    # Print the linked pre_order_traversial_list
    linked_list.print_list()

# Linked pre_order_traversial_list demonstration
def task_3():
    test_linked_list()
    main()


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 4 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


list = [1, 2, 3, 4, 5]

# Takes a pre_order_traversial_list, builds a stack and returns a new pre_order_traversial_list in reverse
def reverse_list(list):
    # Creates empty stack and pre_order_traversial_list
    stack = []
    new_list = []

    # Pushes all elements from pre_order_traversial_list to stack
    for element in list:
        stack.append(element)

    # Pops all elements from stack and adds them to new pre_order_traversial_list
    for element in range(len(stack)):
        new_list.append(stack.pop())

    # Prints new reversed pre_order_traversial_list
    print(new_list)


def task_4():
    reverse_list(list)
    main()


# ---------------------------------------------------------------------------------------------------------------------------------------
# --- Run Assignment --------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------


def main():
    print('\nAvaliable runnable tasks:\n' + '1 :: Task 1' + '\n' + '2 :: Task 2' +
          '\n' + '3 :: Task 3' + '\n' + '4 :: Task 4' + '\n' + 'x :: Exit')
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


def invalid_task():
    print("Invalid task number. Please try again.")
    main()


# This tells python where to start the program
if __name__ == "__main__":
    main()
