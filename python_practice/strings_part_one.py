# -*- coding: utf-8 -*-


def is_my_argument_a_string(maybe_string):
    """In this challenge you need check to see what type of object
    the variable 'maybe_string' is.  If it is a string type please return a true
    if it is not a string object please return false.
    """

    return isinstance(maybe_string, str)


def concatonate_my_arguments(one, two, three):
    """In this challenge you need to concatenate all the arguments together and return the result
    The arguments will always be strings
    """
    return one + two + three

def all_numbers(maybe_string_with_numbers):
    """In this challenge you need to return true if all of the characters in 'maybe_string_with_numbers' are numbers
    if all of the characters in the string are not numbers please return false
    """
    return str.isdigit(maybe_string_with_numbers)

def substring_test(substring, string):
    """In this challenge please return true if the string in the variable 'substring' is contained
    in the string that is in the variable.  If it is not return false.
    Example where you return True:
        substring = 'foo'
        string = 'foobar'
    """
    return str.casefold(substring) in str.casefold(string)

