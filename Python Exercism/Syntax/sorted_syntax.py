# sorted_syntax.py
# Reference sheet for the sorted() builtin


# --- basic syntax ---
# sorted(iterable, key=None, reverse=False) -> new list (does NOT sort in place)
nums = [3, 1, 4, 1, 5, 9, 2]
sorted(nums)                              # -> [1, 1, 2, 3, 4, 5, 9]        (ascending, default)
sorted(nums, reverse=True)                # -> [9, 5, 4, 3, 2, 1, 1]        (descending)

words = ["banana", "apple", "cherry"]
sorted(words)                             # -> ['apple', 'banana', 'cherry']  (alphabetical)

text = "dcba"
sorted(text)                              # -> ['a', 'b', 'c', 'd']         (works on any iterable, even a string)


# --- key: control WHAT gets compared, not the comparison itself ---
words = ["fig", "apple", "kiwi", "banana"]
sorted(words, key=len)                    # -> ['fig', 'kiwi', 'apple', 'banana']  (shortest to longest)
sorted(words, key=len, reverse=True)      # -> ['banana', 'apple', 'kiwi', 'fig']

mixed_case = ["Banana", "apple", "Cherry"]
sorted(mixed_case)                        # -> ['Banana', 'Cherry', 'apple']  (uppercase sorts before lowercase -- ASCII order)
sorted(mixed_case, key=str.lower)         # -> ['apple', 'Banana', 'Cherry']  (case-insensitive sort)


# --- key with lambda: sort by a computed/derived value ---
pairs = [("e", 120), ("a", 95), ("z", 3)]
sorted(pairs, key=lambda pair: pair[1])              # -> [('z', 3), ('a', 95), ('e', 120)]   (by 2nd item, ascending)
sorted(pairs, key=lambda pair: pair[1], reverse=True) # -> [('e', 120), ('a', 95), ('z', 3)]  (by 2nd item, descending)
sorted(pairs, key=lambda pair: pair[0])              # -> [('a', 95), ('e', 120), ('z', 3)]  (by 1st item)


# --- key with operator module: same result, no lambda ---
from operator import itemgetter, attrgetter
sorted(pairs, key=itemgetter(1), reverse=True)       # -> same as the lambda version above
sorted(pairs, key=itemgetter(0))                     # -> sort by 1st item


# --- sorting a dictionary ---
stats = {"e": 120, "a": 95, "z": 3}
sorted(stats)                                        # -> ['a', 'e', 'z']            (bare dict -> sorts KEYS only)
sorted(stats.items())                                # -> [('a', 95), ('e', 120), ('z', 3)]   (sorted by key, since tuples compare left-to-right)
sorted(stats.items(), key=lambda kv: kv[1])          # -> [('z', 3), ('a', 95), ('e', 120)]   (sorted by VALUE, ascending)
sorted(stats.items(), key=lambda kv: kv[1], reverse=True)  # -> [('e', 120), ('a', 95), ('z', 3)]  (by value, descending -- most common first)
sorted(stats, key=stats.get, reverse=True)           # -> ['e', 'a', 'z']            (keys only, ordered by their value)


# --- multiple sort keys (tie-breaking) ---
people = [("Sam", 25), ("Ana", 30), ("Sam", 20)]
sorted(people, key=lambda p: (p[0], p[1]))           # -> [('Ana', 30), ('Sam', 20), ('Sam', 25)]
                                                       # sorts by name first, then by age to break ties among equal names


# --- sorting objects by attribute ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people_objs = [Person("Sam", 25), Person("Ana", 30)]
sorted(people_objs, key=attrgetter("age"))           # -> sorted by .age, ascending
sorted(people_objs, key=lambda p: p.age)             # -> same result, lambda style


# --- sorted() vs list.sort() ---
nums = [3, 1, 2]
sorted(nums)                              # -> [1, 2, 3]   -- returns a NEW list; `nums` is still [3, 1, 2]
nums.sort()                               # -> None        -- sorts IN PLACE; `nums` is now [1, 2, 3]; no return value to assign


# --- Notes ---
# - sorted() works on any iterable (list, tuple, dict, set, string) and always returns a list.
# - Default order is ascending; pass reverse=True for descending.
# - key= takes a FUNCTION (not a called value) -- pass `len`, `str.lower`, `itemgetter(1)`, or a lambda,
#   never `len(x)` or `stats.get(x)`.
# - Sorting is stable: elements that compare equal keep their original relative order
#   (this is what makes the "sort by A, tie-break by B" trick work when done as sorted(x, key=lambda i: (i.a, i.b))).
# - dict.items() gives (key, value) tuples; tuples sort left-to-right by default, so
#   sorted(d.items()) sorts by key unless you supply key=lambda kv: kv[1] to sort by value instead.
