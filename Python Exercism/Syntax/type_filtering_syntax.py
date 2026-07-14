# type_filtering_syntax.py
# Reference sheet for removing/keeping specific types in a mixed-type list

mixed = [1, "two", 3.0, "four", 5, None, True]


# --- Keep only one type (list comprehension) ---
only_ints = [x for x in mixed if isinstance(x, int)]        # -> [1, 5, True]  (bool is a subclass of int!)
only_strs = [x for x in mixed if isinstance(x, str)]          # -> ["two", "four"]
only_ints = [x for x in mixed if type(x) is int]        # -> [1, 5]  (bool is excluded)
# To translate the above compacted comprehension syntax:
"""
        only_ints = []
        for x in nums:
            if type(x) is int:
                only_ints.append(x)
        
only_ints — variable. Correct.
= — it means "assign whatever is on the right side to the name on the left side." 
[...] — this is the list comprehension syntax itself. 
x — expression that gets evaluated and placed into the new list for each iteration that passes the filter.
for x in nums — iterates over nums, and on each pass, the current item is temporarily bound to the name x.
if type(x) is int — filter condition, checked on every iteration. Only when it evaluates to True does the current x get included in the output list.
"""

mixed = [1, 2, 3, 4, 5, 6]

# ---filter only, no transformation---
evens = [x for x in mixed if x % 2 == 0]
# appends to the list [2, 4, 6]

# ---filter, then transform---
doubled_evens = [x * 2 for x in mixed if x % 2 == 0]
# appends to the list [4, 8, 12]

# ---filter, then transform into something else entirely---
labeled = [f"even: {x}" for x in mixed if x % 2 == 0]
# appends to the list ['even: 2', 'even: 4', 'even: 6']

# --- Exclude one type ---
no_strings = [x for x in mixed if not isinstance(x, str)]    # -> [1, 3.0, 5, None, True]


# --- Exclude/keep multiple types at once (tuple of types) ---
cleaned = [x for x in mixed if not isinstance(x, (str, type(None)))]   # drop str and None


# --- Exclude bools when filtering ints (bool is a subclass of int) ---
true_ints = [x for x in mixed if isinstance(x, int) and not isinstance(x, bool)]  # -> [1, 5]


# --- filter() version (same idea, lazy iterator) ---
only_ints2 = list(filter(lambda x: isinstance(x, int), mixed))


# --- Removing in place, safely (iterate over a copy) ---
for item in mixed[:]:              # mixed[:] copies the list so mutating mixed is safe
    if isinstance(item, str):
        mixed.remove(item)         # removes by value, not index -- order-safe


# --- type() vs isinstance() ---
type(5) == int                     # works, but doesn't account for subclasses
isinstance(5, int)                  # preferred -- also matches subclasses (e.g. bool)
isinstance(True, int)                # True -- bools ARE ints in Python


# --- Notes ---
# - Prefer isinstance() over type() == checks -- handles inheritance correctly.
# - Never mutate a list (pop/remove/del) while iterating over the ORIGINAL list --
#   it skips elements because indices shift. Iterate a copy (mixed[:]) or build a new
#   list with a comprehension instead.
# - List comprehensions don't mutate anything, so they're the safest default for filtering.
