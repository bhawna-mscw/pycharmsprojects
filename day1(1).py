"""
WAP to find the smallest, largest number from the list of entered numbers.
"""
numberlist=[]
number=int(input("How many numbers are there:"))
for i in range(1,number+1):
    value=int(input("Enter number:"))
    numberlist.append(value)
print("Largest element of the list is :", max(numberlist))
print("Smallest element of the list is: ", min(numberlist))
