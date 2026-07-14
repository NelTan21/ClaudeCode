for item in iterable:
    ...

for i in range(start, stop, step):
    ...

for i in range(stop):
    ...

for index, value in enumerate(iterable):
    ...

# Examples:

for fruit in ["apple", "banana"]:
    print(fruit)

for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

for i in range(2, 10, 2):
    print(i)   # 2, 4, 6, 8

################################################
for i, fruit in enumerate(["apple", "banana"]):
    print(i, fruit)
"""
enumerate() gives a 2-item pair:
(index, value)
Not more than that.
So this works:
"""

for i, fruit in enumerate(["apple", "banana"]):
    print(i, fruit)

# But this would fail:

for a, b, c in enumerate(["apple", "banana"]):
    print(a, b, c)

"""
because each item from enumerate() only has 2 values.
If you need more values, they usually come from the item itself being a tuple, like:
"""

pairs = [("apple", "red"), ("banana", "yellow")]

for i, (fruit, color) in enumerate(pairs):
    print(i, fruit, color)

# That works because enumerate() gives:

(0, ("apple", "red"))
(1, ("banana", "yellow"))