num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    result = 0
else: 
    result = num1 + num2 + num3
print("The calculated sum is:", result)
