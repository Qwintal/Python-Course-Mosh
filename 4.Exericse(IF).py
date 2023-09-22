# Price of a house is $1M.
# If buyer has good credit,
# they need to put down 10%
# otherwise
# they need to put down 20%
# print the down payment

Price_Of_House = 1000000
Good_Credit = False

if Good_Credit:
 Down_Payment = Price_Of_House * 0.1

else:
 Down_Payment = Price_Of_House * 0.2

print(f"Down Payment will be ${Down_Payment}")
