def find_max(numbers):
    max_val = numbers[0]
    for number in numbers:
        if number > max_val:
            max_val = number
    return max_val
