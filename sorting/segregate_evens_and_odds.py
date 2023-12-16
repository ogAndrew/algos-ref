def segregate_evens_and_odds(numbers):
    n = len(numbers)

    left = 0
    right = n - 1

    while right >= left:
        num = numbers[right]

        if num % 2 == 0:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
        else:
            right -= 1

    return numbers
