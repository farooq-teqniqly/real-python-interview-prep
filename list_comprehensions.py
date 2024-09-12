def create_grid(num_rows: int, num_cols: int) -> list:
    """
        Creates a grid of num_rows x num_cols.

    >>> create_grid(2, 3)
    [[0, 0, 0], [0, 0, 0]]

    >>> create_grid(1, 1)
    [[0]]

    >>> create_grid(3, 2)
    [[0, 0], [0, 0], [0, 0]]
    """
    return [[0 for _ in range(num_cols)] for _ in range(num_rows)]

def is_odd(x: int):
    """
        Returns True if x is odd, False otherwise.
    >>> is_odd(1)
    True

    >>> is_odd(0)
    False

    >>> is_odd(2)
    False
    """
    return x % 2 == 1

numbers = list(range(1, 11, 1))

odd_numbers = [n for n in numbers if is_odd(n)]

print(odd_numbers)
print(any(is_odd(n) for n in odd_numbers))
print(all(is_odd(n) for n in odd_numbers))
print(all(is_odd(n) for n in numbers))
