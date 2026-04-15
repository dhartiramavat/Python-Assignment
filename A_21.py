# Program to add 'in' or 'ly' to a string based on specific conditions
user_input = input("Enter a string: ")


if len(user_input) < 3:
    result = user_input

elif user_input.endswith('ing'):
    result = user_input + 'ly'

else:
    result = user_input + 'in'

print("Resulting string:", result)
