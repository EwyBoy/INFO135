# 18.02.2022 - Laget av Eivind Norling

# Har laget oppgaven som en kjørbar fil.
# Task 1 til 4 kan alle kjøres med denne filen i terminalen.

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 1 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------


task_1_list = [1001, 1030, 1050, 1020, 300, 1080, 1100]

# Selection Sort
def task_1():
    selection_sort(task_1_list)
    main()

# selection sort and break after 3 passes
def selection_sort(sort_list):
    for i in range(len(sort_list)):
        min_index = i
        for j in range(i+1, len(sort_list)):
            if sort_list[min_index] > sort_list[j]:
                min_index = j
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]
        print("Pass: " + str(i + 1), sort_list)
        if i >= 2:
            break
    return sort_list

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 2 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

task_2_list = [210, 15, 111, 90, 45, 120, 150, 200, 100, 140]

# Boble sort
def task_2():
    boble_sort(task_2_list)
    main()    

# Boble sort and break after 3 passes
def boble_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort) - 1, i, -1):
            if list_to_sort[j] < list_to_sort[j - 1]:
                list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]
                print("Pass: " + str(i + 1), list_to_sort)
            else:
                break
        print("Pass: " + str(i + 1), list_to_sort)    
        if i >= 2:
            break       

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 3 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

task_3_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]

def task_3():
    print(sort_and_rem_dup(task_3_list)) 
    main()   


# Sort & remove duplicates
def sort_and_rem_dup(list_to_sort):
    list_to_sort = insertion_sort(list_to_sort)
    list_to_sort = remove_duplicates(list_to_sort)
    return list_to_sort


# Decided to use insertion sort here cause have already used bubble sort and selection sort
def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
            j = i
            while j > 0 and list_to_sort[j] < list_to_sort[j - 1]:
                list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]
                j -= 1
    return list_to_sort   


# Removes duplicates from list
def remove_duplicates(list_to_filter):
    for i in range(len(list_to_filter)):
            for j in range(i + 1, len(list_to_filter)):
                if list_to_filter[i] == list_to_filter[j]:
                    list_to_filter.pop(j)
                    break
    return list_to_filter

# -------------------------------------------------------------------------------------------------------------------------------
# --- Task 4 --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

word_list = ['radar', 'hello', 'civic', 'info134',  'agnes i senga']

def task_4():
    print('-------------------------------------------------------------------------------------------------------------------------------')
    for word in word_list:
        print(word, " | ", check_palindrome(word))
        print('-------------------------------------------------------------------------------------------------------------------------------')
    main()    


def check_palindrome(word):
    """ Check if word is a palindrome stack queue """

    # Create empty stack and queue
    stack = []
    queue = []

    # Push all characters to stack
    for character in word:
        stack.append(character)

    # Push all characters to queue
    for character in word:
        queue.append(character)

    # Pop all characters from stack and add them to new list
    new_list = []
    for character in range(len(stack)):
        new_list.append(stack.pop())

    # Pop all characters from queue and add them to new list
    for character in range(len(queue)):
        new_list.append(queue.pop(0))

    # Now split new list in half and compare the two halves
    half_list = len(new_list) // 2

    first_half = new_list[:half_list]
    second_half = new_list[half_list:]

    print(first_half, " | ", second_half)

    # Check if first half is equal to second half
    if first_half == second_half:
        return True
    else:
        return False



# -------------------------------------------------------------------------------------------------------------------------------

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


def invalid_task():
    print("Invalid task number. Please try again.")
    main()

if __name__ == "__main__":
    main()
