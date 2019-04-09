def int_to_hex(digit: int, to_string: dict) -> str:
    """Convert int to hexidecimal string."""

    result = ''

    while digit > 0:
        remainder = digit % 16
        result = to_string[remainder] + result
        digit = digit // 16

    return result


def string_to_hex(word: str, hex_dict: dict) -> str:
    """Function to convert string input into its equivalent hexidecimal string.

    input: input string to be converted to hexidecimal
    """
    # Format the string to be all lowercase and remove any spaces
    word = word.lower()
    word = word.replace(' ', '')

    result = ''
    for char in word:
        # Convert char to its ASCII int value with ord() and convert that to hex
        hex_str = int_to_hex(ord(char), hex_dict)
        result += hex_str

    return result


def nth_digit() -> int:
    """Function that calculates the Nth digit of Pi in hex.

    Uses BBP formula
    """
    a, b = 0, 1
    k = 0
    while True:
        ak, bk = (120 * k**2 + 151 * k + 47,
                  512 * k**4 + 1024 * k**3 + 712 * k**2 + 194 * k + 15)
        a, b = (16 * a * bk + ak * b, b * bk)
        digit, a = divmod(a, b)
        yield digit
        k = k + 1


def find_string(target: str, hex_dict: dict) -> tuple:
    """ Looks for the given string, in hexidecimal form, as a substring of pi, also in hex.

    positional arguments:
    target: string that will be searched for in pi
    hex_dict: dictionary used to convert int values into their hex equivalents as a string
    """

    pi = nth_digit()
    word = string_to_hex(target, hex_dict)
    # Starting index of the target string
    start = -1
    # Ending index of the target string
    end = -1

    # Current index of the target string that we are looking for
    # THIS IS NOT THE CURRENT INDEX OF PI THAT WE ARE ON
    # The current index of pi that we are on is handled by i in the enumerate function
    current_index = 0

    for i, digit in enumerate(pi):
        # Current index is equal to the length of the target string
        # This means that the target has been found and the last char is the 1 - the index of the current char
        if current_index == len(word):
            end = i - 1
            break
        if hex_dict[digit] == word[current_index]:
            # Found a the first letter of target string
            if current_index == 0:
                start = i
            current_index += 1
        else:
            # Where we are in Pi does not match the current index of the target string we are looking for
            # Reset start, end, and current indecies
            current_index = 0
            start = -1
            end = -1
    return (start, end)


def main():
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3',
                4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'a', 11: 'b',
                12: 'c', 13: 'd', 14: 'e', 15: 'f'
                }

    target = input('Enter a string to search for in Pi: ')
    start, end = find_string(target, hex_dict)
    print(f'{target} is located from {start} to {end} in Pi')


main()
