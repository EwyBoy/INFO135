# 26.02.2022 - Laget av Eivind Norling

# Har laget oppgaven som en kjørbar fil.
# Task 1 til 4 kan alle kjøres med denne filen i terminalen.

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 1 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

# The printed output of the following code is: 
# 79166 or 7 9 16 6
# Depends on the end='' parameter of the print function.
# I am not sure if there should be a space there or not..

my_list = ['alb2c3', 'CiTiBnk', '232323', 'myLaptop']
my_choice = 19

def task_1():
    for item in my_list:
        print(hash_function(item, my_choice), end='')    
    main()

def hash_function (input_string, table_size):
    total = 0 
    length = len(input_string) 
    for pos in range (length):
        total = total + ord (input_string[pos]) + length 
    return total % table_size


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 2 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

import random as rand
import hashlib as hash

def task_2():
    my_hash = HashClass(11011999)
    my_hash.print_it()
    main()

class HashClass:

    # -- Constructor --
    # Takes in a number and creates a hash table with that size
    def __init__(self, id_num):
        # Calling the hash_it function
        self.hash_value = self.hash_it(id_num)

    def hash_it(self, id_num):
        # Generating salt as a random number between 0 and 1000
        salt = rand.randint(0, 1000)
        # Salting the id_num with the salt
        id_num = str(id_num + salt)
        # Hashing the salted id_num
        hash_object = hash.sha1(id_num.encode('utf-8'))
        # Returning the hash value
        return hash_object.hexdigest()

    # Prints the hash value
    def print_it(self):
        print(self.hash_value)


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 3 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

list_of_tuples = [
    ('Birds of Pray', 97.1),
    ('Dolittle', 175.0),
    ('The Gentlemen', 7.0),
    ('Falling', 22.0)
]

def task_3():
    sort_and_print(list_of_tuples)
    main()

# sorts the list of tuples by the second element in the tuple
def sort_and_print(tuple_list_to_sort):
    for i in range(1, len(tuple_list_to_sort)):
        j = i
        # while the element in the tuple is less than the element in the tuple before it
        while j > 0 and tuple_list_to_sort[j][1] < tuple_list_to_sort[j - 1][1]:
            # swap the elements
            tuple_list_to_sort[j], tuple_list_to_sort[j - 1] = tuple_list_to_sort[j - 1], tuple_list_to_sort[j]
            j -= 1    
    print('The movie with the largest budget is:' + '\n' + tuple_list_to_sort[-1][0])


# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 4 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

def task_4():
    print(magic_function('abcd'))
    main()

# finds all the permutations of any given string
def magic_function(text_to_permute):
    # if the string is of length 1, return the string
    if len(text_to_permute) == 1:
        return [text_to_permute]
    else:
        # create an empty list to store the permutations
        permutations = []
        # for each character in the string
        for i in range(len(text_to_permute)):
            # get the character
            first_char = text_to_permute[i]
            # get the permutations of the remaining characters
            remaining_chars = text_to_permute[:i] + text_to_permute[i+1:]
            # for each permutation of the remaining characters
            # use recursion to get all the permutations
            for permutation in magic_function(remaining_chars):
                # add the current permutation to the list of permutations
                permutations.append(first_char + permutation)
        # return the list of permutations        
        return permutations


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