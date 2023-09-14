# Enter weight in lbs or kg and convert in other unit
# Should not be case-sensitive

Weight = int(input("Weight in number:"))
unit = input("(L)bs or (K)g:")

if unit.upper() == "L":
    weight_kilo = Weight * 0.45
    print(f"You are {weight_kilo} kilograms.")

else:
    weight_pound = Weight / 0.45
    print(f"You are {weight_pound} pounds.")

