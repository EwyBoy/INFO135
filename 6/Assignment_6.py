# 04.21.2022 - Laget av Eivind Norling

# Har laget oppgaven som èn kjørbar fil.
# Task 1 til 4 kan alle kjøres med denne filen i terminalen.

# ----------------------------------------------------------------------------------------------------------------------
# --- Task 1 -----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

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


def build_binary_tree():
    node_a = BinaryTree('A')
    node_a.insert_left('B')
    node_a.insert_right('C')

    node_b = node_a.left
    node_b.insert_left('D')
    node_b.insert_right('E')

    node_c = node_a.right
    node_c.insert_left('F')

    node_d = node_b.left
    node_d.insert_left('G')
    node_d.insert_right('H')

    node_e = node_b.right
    node_e.insert_right('I')

    node_f = node_c.left
    node_f.insert_left('J')

    return node_a


pre_order_traversal_list = []


def pre_order_traversal(node):
    if node is not None:
        pre_order_traversal_list.append(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


answer_options = {
    'A': 'A B D G H E I C F J ',
    'B': 'A B C D E F G H I J ',
    'C': 'G H D I E B J F C A ',
    'D': 'G D H B E I A J F C ',
}


# list into string
def list_to_string(my_list):
    string = ''
    for item in my_list:
        string += item + ' '
    return string


def task_1():
    print('Task 1:')
    node = build_binary_tree()
    pre_order_traversal(node)

    my_answer = list_to_string(pre_order_traversal_list)

    found_answer = False

    for key, value in answer_options.items():
        if my_answer == value:
            found_answer = True
            print('Alternative -> ' + key + ' : ' + value + ' is correct!')
        else:
            print('Alternative -> ' + key + ' : ' + value + ' is incorrect!')

    if not found_answer:
        print('Alternative E -> "None of them" is correct!')

    main()


# ----------------------------------------------------------------------------------------------------------------------
# --- Task 2 -----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Write a class called QuizGift that has a method compute_result() to
# solve the following problem and to compute the result. Then, write another
# method called print_result() that prints out the result.

# Sara is going to attend a written quiz where she can receive a prize based
# on the number of points she obtains. The written quiz has 5 questions each
# of them is worth different points and each takes different amount of time to
# answer. Sara will have 100 minutes and can choose which subset of
# questions to answer from the following question set:

# Question 1 has 120 points and it takes 15 minutes to answer
# Question 2 has 200 points and it takes 20 minutes to answer
# Question 3 has 150 points and it takes 40 minutes to answer
# Question 4 has 350 points and it takes 50 minutes to answer
# Question 5 has 100 points and it takes 20 minutes to answer
# Question 6 has 90 points and it takes 10 minutes to answer

# Sara will receive a watch if she obtains up to 250 points, a smartphone if
# she obtains 250 - 750 points, and, a laptop if she obtains more than 750
# points. Sara would like to have a Python program, based on Dynamic
# Programming, to compute the maximum number of points she can obtain (in
# the given time) and to print it out. The program should also print the gift
# that she will receive as the result of answering the quiz. Please help her!

# Note: You can write more methods in the QuizGift class if needed.

class QuizGift:
    gift_prices = ['Watch', 'Smartphone', 'Laptop']

    def __init__(self):
        self.question_set = [
            [120, 15],
            [200, 20],
            [150, 40],
            [350, 50],
            [100, 20],
            [90, 10],
        ]

    def compute_result(self):
        self.max_points = 0
        self.max_points_time = 0

        for i in range(len(self.question_set)):
            for j in range(i, len(self.question_set)):
                points = 0
                time = 0
                for k in range(i, j + 1):
                    points += self.question_set[k][0]
                    time += self.question_set[k][1]

                if time <= 100 and points > self.max_points:
                    self.max_points = points
                    self.max_points_time = time

        return self.max_points, self.max_points_time

    def find_gift(self, points):
        if points <= 250:
            return self.gift_prices[0]
        elif points <= 750:
            return self.gift_prices[1]
        else:
            return self.gift_prices[2]

    def print_result(self):
        result = self.compute_result()
        print('The maximum number of points that Sara can obtain is: ' + str(result))
        gift = self.find_gift(result[0])
        print('Gift received: {}'.format(gift))


def task_2():
    print('Task 2:')
    gift = QuizGift()
    gift.print_result()
    main()


# ----------------------------------------------------------------------------------------------------------------------
# --- Task 3 -----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

from abc import abstractmethod


class Shape:

    @abstractmethod
    def compute_area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def compute_area(self):
        area = self.side ** 2
        return print(area)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        area = 3.14 * self.radius ** 2
        return print(area)


class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def compute_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        area = (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5
        return print(area)


def task_3():
    print('Task 3')
    my_square = Square(2)
    print('Square area: ', end=' ')
    my_square.compute_area()

    my_circle = Circle(2)
    print('Circle area: ', end=' ')
    my_circle.compute_area()

    my_triangle = Triangle(5, 4, 3)
    print('Triangle area: ', end=' ')
    my_triangle.compute_area()

    main()


# ----------------------------------------------------------------------------------------------------------------------
# --- Task 4 -----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class House:
    count = 0

    def __init__(self, owner, condition, price):
        self.owner = owner
        self.condition = condition
        self.price = price
        self.cost = 0
        self.sold = False
        House.count += 1

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        print('House sold! Profit: ', self.price - self.cost)

    def change_price(self, new_price):
        if self.sold:
            print('House has been sold!')
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost += expense
        self.condition = new_condition
        print('House renovated!')

    def print_info(self):
        print('Owner: ', self.owner, ', Condition: ', self.condition, ', Price: ', self.price)


def task_4():
    print('Task 4:')

    house1 = House('John', 'Good', 100000)
    house2 = House('Mary', 'Bad', 250000)

    print('')

    house1.print_info()
    house2.print_info()

    print('')

    house1.renovate(50000, 'Great')
    house1.sell('Leo')

    print('')

    house1.print_info()

    print('Total number of houses: ', House.count)

    main()


# ----------------------------------------------------------------------------------------------------------------------

# Runnable launcher
def main():
    print(
        '\n'
        'Available runnable tasks:\n' +
        '1 :: Task 1\n' +
        '2 :: Task 2\n' +
        '3 :: Task 3\n' +
        '4 :: Task 4\n' +
        'x :: Exit'
    )

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

# ----------------------------------------------------------------------------------------------------------------------
