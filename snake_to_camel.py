"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""


def snake_to_camel(variable_name):
    word_list = variable_name.split("_")

    if len(word_list) <= 1:
        return variable_name
    else:
        result = word_list[0]
        for idx in range(1, len(word_list)):
            result += word_list[idx].capitalize()
    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
