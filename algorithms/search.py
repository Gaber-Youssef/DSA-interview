def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    time complexity: O(n)
    space complexity: O(1)
    is in-place: Yes
    is stable: Yes
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    time complexity: O(logn)
    space complexity: O(1)
    is in-place: Yes
    is stable: Yes
    """
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None