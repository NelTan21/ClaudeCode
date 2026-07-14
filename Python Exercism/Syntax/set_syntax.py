# set_syntax.py
# Reference sheet for Python set syntax and operations


# --- Creating a set ---
s = {1, 2, 3}                   # set literal
s = set()                       # empty set (NOT {} -- that's an empty dict)
s = set([1, 2, 3])              # from a list
s = set((1, 2, 3))              # from a tuple
s = set("abc")                  # {'a', 'b', 'c'} -- from any iterable
s = {x for x in range(5)}       # set comprehension
s = {x * 2 for x in range(5) if x % 2 == 0}  # comprehension with condition

fs = frozenset([1, 2, 3])       # immutable set (hashable, usable as dict key)


# --- Adding / removing elements ---
s.add(4)                        # add a single element
s.update([4, 5, 6])              # add multiple elements from an iterable
s.update([7, 8], {9, 10})        # update accepts multiple iterables

s.remove(4)                     # remove element; raises KeyError if missing
s.discard(4)                    # remove element; no error if missing
s.pop()                         # remove and return an arbitrary element; raises KeyError if empty
s.clear()                       # remove all elements


# --- Membership / size ---
3 in s                           # True/False membership test
3 not in s                       # inverse membership test
len(s)                           # number of elements


# --- Set algebra ---
a = {1, 2, 3}
b = {2, 3, 4}

a | b                            # union -> {1, 2, 3, 4}
a.union(b)                       # same as above

a & b                            # intersection -> {2, 3}
a.intersection(b)                # same as above

a - b                            # difference -> {1}
a.difference(b)                  # same as above

a ^ b                            # symmetric difference -> {1, 4}
a.symmetric_difference(b)        # same as above


# --- In-place versions (mutate the left-hand set) ---
a |= b                           # a = a.union(b)
a.update(b)                      # equivalent to a |= b

a &= b                           # a = a.intersection(b)
a.intersection_update(b)         # equivalent to a &= b

a -= b                           # a = a.difference(b)
a.difference_update(b)           # equivalent to a -= b

a ^= b                           # a = a.symmetric_difference(b)
a.symmetric_difference_update(b) # equivalent to a ^= b


# --- Comparisons ---
a <= b                           # a is subset of b (or equal)
a.issubset(b)                    # same as above
a < b                            # a is a proper subset of b

a >= b                           # a is superset of b (or equal)
a.issuperset(b)                  # same as above
a > b                            # a is a proper superset of b

a.isdisjoint(b)                  # True if a and b share no elements

a == b                           # sets are equal (same elements, order irrelevant)
a != b                           # sets are not equal


# --- Copying ---
c = a.copy()                     # shallow copy of a set


# --- Conversion ---
list(a)                          # convert set to list (order not guaranteed)
sorted(a)                        # convert set to sorted list
tuple(a)                         # convert set to tuple


# --- Iteration ---
for item in a:                   # iterate over elements (order not guaranteed)
    pass


# --- Common idioms ---
unique_items = list(set([1, 2, 2, 3, 3, 3]))          # dedupe (order NOT preserved)
ordered_unique = list(dict.fromkeys([1, 2, 2, 3]))     # dedupe (order preserved)

seen = set()
for item in [1, 2, 2, 3]:
    if item not in seen:
        seen.add(item)


# --- Notes ---
# - Sets are unordered and mutable; elements must be hashable (no lists/dicts/sets inside).
# - frozenset is the immutable counterpart; it is itself hashable and can be used as a dict key
#   or nested inside another set.
# - Membership tests (`in`) are O(1) average for sets vs O(n) for lists.
