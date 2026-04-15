# Print Fibonacci numbers up to a specific value
limit = 100
a, b = 0, 1

print("Fibonacci numbers under 100:")
while a < limit:
    print(a, end=" ")
    a, b = b, a + b
