# Input strings
str1 = 'abc'
str2 = 'xyz'

# Slicing to swap the first two characters
# Take first 2 from str2 and add the rest of str1
new_str1 = str2[:2] + str1[2:]

# Take first 2 from str1 and add the rest of str2
new_str2 = str1[:2] + str2[2:]

# Combine with a space separator
result = new_str1 + " " + new_str2

# Output the final single string
print(result)  