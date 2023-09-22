# Write a program to find the largest number in a list.

numbers = [1, 2, 3, 4, 5, 10]
maximum_number = numbers[0]

for number in numbers:
    if number > maximum_number:
        maximum_number = number

print(maximum_number)


