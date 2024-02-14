# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 8/3/2023
# Description: Defines a function named count_letters that takes a string as a parameter and
# returns a dictionary that tabulates how many of each letter is in that string.


def count_letters(sample_text):
    """
    takes a string as a parameter and returns a dictionary that
    tabulates how many of each letter is in that string.
    The string can contain characters other than letters.
    Lower-case and upper-case versions of a letter are treated as one.
    :param sample_text: string
    :return: dictionary
    """
    upper_text = sample_text.upper()  # Converts the argument to uppercase to avoid seperate lower and upper counts
    string_list = []  # Creates an empty list
    result_dict = {}  # Creates an empty dictionary
    for letter in upper_text:  # iterates for each letter in the string
        if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if letter in string_list:  # Checks if letter is already in string
                result_dict[letter] += 1  # adds one to existing value in dictionary
            else:  # Runs if the letter is not in dictionary
                string_list.append(letter)  # Adds the letter to the string
                result_dict[letter] = 1  # Adds the letter to the dictionary as a key and sets the value to 1
    return result_dict
