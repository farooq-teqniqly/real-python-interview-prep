from typing import List


def get_max(numbers: List[int]) -> int:
    """
        Returns the largest number in the list.

        >>> get_max([-1000, 400, -90000, 99999, 5454])
        99999
    """
    max_num = float("-inf")

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num
