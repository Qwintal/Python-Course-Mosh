# Write a program to remove the duplicates in a lists.
numbers = [1, 2, 1, 4, 2, 4, 51, 51, 2, 2, 2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)

# Don't try to modify list by removing elements while iterating over it, it will lead
# unexpected behaviour as list is changing size during iteration.
