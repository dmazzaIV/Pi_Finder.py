import pytest
import pi_finder


hex_dict = {0: '0', 1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'a', 11: 'b',
            12: 'c', 13: 'd', 14: 'e', 15: 'f'
            }


# def test_nth_digit():
#     """ Test that I can calculate pi to the 10^6 decimal place accurately.
#     DO NOT RUN THIS TEST UNLESS YOU HAVE A LOT OF TIME!!!!!!!!!!!!
#     IT TAKES ABOUT 5 HOURS TO RUN.
#     There is a screenshot of it passing on github if you do not believe me.
#     """
#     pi_generator = pi_finder.nth_digit()
#     with open('mil_digits.txt') as pi:
#         for line in pi:
#             for char in line:
#                 assert hex_dict[next(pi_generator)] == char


def test_int_to_hex():
    """ Test that all lowercase letters are properly converted to their hex values."""
    hex_values = ['61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f',
                  '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']
    index = 0
    for x in range(97, 123):
        assert pi_finder.int_to_hex(x, hex_dict) == hex_values[index]
        index += 1


def test_string_to_hex():
    """ Test that strings are properly converted to their hexidicimal eqivalents."""
    strings = ['helloworld', 'HelloWorld', 'HELLOWORLD', 'Hello WorLd', 'hElLo W Or L d', 'h e l l o w o r l d']

    for i, word in enumerate(strings):
        assert pi_finder.string_to_hex(word, hex_dict) == '68656c6c6f776f726c64'


def test_find_string():
    """ Test that a certian substring can be found in a given string."""
    assert pi_finder.find_string('j', hex_dict) == (5, 6)
    assert pi_finder.find_string('l', hex_dict) == (61, 62)
    assert pi_finder.find_string('c', hex_dict) == (72, 73)
