def dutch_flag_sort(balls):
    n = len(balls)
    red = -1
    green = -1

    for blue in range(len(balls)):
        if balls[blue] == "G":
            green += 1
            swap(balls, green, blue)
        elif balls[blue] == "R":
            green += 1
            swap(balls, green, blue)
            red += 1
            swap(balls, red, green)

    return balls


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# alternative
def dutch_flag_sort(balls):
    n = len(balls)

    left = 0
    right = n - 1
    mid = left

    while mid <= right:
        if balls[mid] == "R":
            balls[left], balls[mid] = balls[mid], balls[left]
            left += 1
            mid += 1
        elif balls[mid] == "B":
            balls[right], balls[mid] = balls[mid], balls[right]
            right -= 1
        else:
            mid += 1

    return balls
