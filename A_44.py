# Create a tuple with different data types
mixed_tuple = ("Hello", 42, 3.14, True, [1, 2, 3])

# Print the entire tuple
print("Mixed Tuple:", mixed_tuple)

# Check the data type of each element
print("\nElement types:")
for item in mixed_tuple:
    print(f"Value: {item} | Type: {type(item)}")
