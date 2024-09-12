def fizz_buzz(numbers: list):
    """
        Modify the list of numbers replacing multiples of 3 with "fizz",
        multiples of 5 with "buzz", and multiples of both 3 and 5 with "fizzbuzz".

        >>> nums = [1, 2, 3, 4, 5, 15]
        >>> fizz_buzz(nums)
        >>> nums
        [1, 2, 'fizz', 4, 'buzz', 'fizzbuzz']

        >>> nums = [3, 5, 9, 10, 30]
        >>> fizz_buzz(nums)
        >>> nums
        ['fizz', 'buzz', 'fizz', 'buzz', 'fizzbuzz']

        >>> nums = []
        >>> fizz_buzz(nums)
        >>> nums
        []
    """
    for i in range(len(numbers)):
        if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
            numbers[i] = "fizzbuzz"
            continue

        if numbers[i] % 3 == 0:
            numbers[i] = "fizz"
            continue

        if numbers[i] % 5 == 0:
            numbers[i] = "buzz"
            continue
