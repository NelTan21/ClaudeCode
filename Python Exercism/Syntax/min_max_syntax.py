# ---- Built-in min() / max() ----

min(1, 5, 3)                 # -> 1
max(1, 5, 3)                 # -> 5

min([1, 5, 3])                # -> 1   (works on any iterable)
max([1, 5, 3])                # -> 5

min("apple", "banana")         # -> "apple"  (works with strings/any comparable type)

words = ["hi", "hello", "hey"]
max(words, key=len)            # -> "hello"  (longest, by key function)
min(words, key=len)            # -> "hi"     (shortest, by key function)

min([], default=0)             # -> 0   (avoids ValueError on empty iterable)

lo, hi = min(nums), max(nums)  # get both at once


# ---- Manual search using float("inf") placeholder ----
#
# Pairing to remember:
#   minimum -> start with float("inf")   (bigger than any real value, always loses)
#   maximum -> start with float("-inf")  (smaller than any real value, always loses)
#
# Rule of thumb: the placeholder is the OPPOSITE extreme of what you're
# looking for, so the first real value always overwrites it.

# Searching for a MINIMUM
smallest = float("inf")
for n in numbers:
    if n < smallest:
        smallest = n

# Searching for a MAXIMUM
largest = float("-inf")
for n in numbers:
    if n > largest:
        largest = n


# ---- float("inf") notes ----

float("inf") > 10**1000        # True  - always bigger than any finite number
float("inf") == float("inf")   # True
float("inf") - float("inf")    # nan   - undefined

# Also used as "not yet reachable" sentinel, e.g. Dijkstra's shortest path:
distances = {node: float("inf") for node in graph}
distances[start] = 0
