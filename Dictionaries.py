# Convert number into words
phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for digit in phone:
    output += digits_mapping.get(digit,"Please enter a 'Number'.") + " "

print(output)