"""
To calculate shipping charges.
"""
amount=int(input("Enter the total amount:"))
if (amount)<50:
    print("Total value:",(amount+10))
else:
    print("Total value:",amount)