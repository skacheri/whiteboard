"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""
    num_dict={}
    num_set = set()
    for i in nums:
        if i in num_dict:
            num_dict[i] = num_dict[i] + 1
        else:
            num_dict[i] = 1
    value_max = max(num_dict.values())

    for key in num_dict:
        if num_dict[key] == value_max:
            num_set.add(key)
    return num_set


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
