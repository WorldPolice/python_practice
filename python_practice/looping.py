# -*- coding: utf-8 -*-


def looping_challenge_one():
    """Print the numbers 1 - 10 using a loop

    Please print each number on a separate line
    ex:
        1
        2
        3
        ...
    """
    numbers = range(1, 11)
    for number in numbers:
        print(number)


def looping_challenge_two():
    """Given the variable colors_of_the_rainbow

    Please print every other color on a separate line
    """
    colors_of_the_rainbow = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
    index = 0
    list_size = len(colors_of_the_rainbow)
    while index < list_size:
        if index % 2 == 0:
            print(colors_of_the_rainbow[index])
        index += 1


def looping_challenge_three():
    """Print the following on separate lines

    The numbers 1 - 4 in acceding order
    The numbers 4 - 1 in descending order

    * Bonus points: accomplish this with only one list that contains only 4 elements
    """

    numbers = [1, 2, 3, 4]
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    for number in ascending:
        print(number)
    for number in descending:
        print(number)
