"""Given a number, convert to look and say format.

For example::

    >>> look_say(1112223)
    '313213'
    >>> look_say(1111)
    '41'

"""
def look_say(number):
    number_string = str(number)
    counter = 0
    char_selected = number_string[0]
    result = ""

    for idx in range(0, len(number_string)):
        if number_string[idx] == char_selected:
            counter += 1
        else:
            result += str(counter)
            result += char_selected
            counter = 1
            char_selected = ""
            char_selected = number_string[idx]
    result += str(counter)
    result += char_selected
    return result




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")

#thoughts:
#iterate over the string of the number
#assign a counter that resets when the number is not equal to current char_selected and stores it in the return string and char_selected becomes next char if not none
#if number is equal then increase counter by 1
#at end check if the counter is not zero then add counter and the char_selected