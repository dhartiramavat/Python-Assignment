
numbers = [10, 24, 76, 23, 12]

# Initialize variables using the first element of the list
# This handles both positive and negative numbers correctly
largest = numbers[0]
smallest = numbers[0]
total_sum = 0

# Iterate through each number in the list
for num in numbers:
    # Update the largest number if current num is bigger
    if num > largest:
        largest = num
    
    # Update the smallest number if current num is smaller
    if num < smallest:
        smallest = num
        
    # Add current number to the running total
    total_sum += num

# Output the results
print("Largest Number:", largest)
print("Smallest Number:", smallest)
print("Sum of all numbers:", total_sum)


