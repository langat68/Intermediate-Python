from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# 1. Square each number (map)
squared = list(map(lambda x: x**2, nums))
print("Squared:", squared)

# 2. Keep even numbers (filter)
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)

# 3. Multiply all numbers (reduce)
product = reduce(lambda x, y: x * y, nums)
print("Product:", product)

# 4. Combine: square even numbers only
square_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print("Square of evens:", square_evens)
