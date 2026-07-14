# list_syntax.py
# Reference sheet for Python list syntax and operations


# --- Creating a list ---
lst = [1, 2, 3]                   # list literal
lst = []                          # empty list
lst = list()                      # empty list (equivalent to [])
lst = list((1, 2, 3))             # from a tuple
lst = list("abc")                 # ['a', 'b', 'c'] -- from any iterable
lst = list(range(5))              # [0, 1, 2, 3, 4]
lst = [x * 2 for x in range(5)]   # list comprehension
lst = [x for x in range(10) if x % 2 == 0]  # comprehension with condition


# --- Adding elements ---
lst.append(4)              # add single element to the end
lst.insert(0, 99)           # insert element at index 0
lst.extend([5, 6])          # append multiple elements from an iterable
lst += [7, 8]               # same effect as extend


# --- Removing elements ---
lst.remove(4)               # remove first occurrence of value; raises ValueError if missing
lst.pop()                   # remove and return last element
lst.pop(0)                  # remove and return element at index 0
del lst[0]                  # delete element at index 0
del lst[1:3]                # delete a slice
lst.clear()                 # remove all elements


# --- Accessing / slicing ---
lst[0]                      # first element
lst[-1]                     # last element
lst[1:3]                    # slice -- elements at index 1, 2
lst[:3]                     # first 3 elements
lst[::2]                    # every 2nd element
lst[::-1]                   # reversed copy


# --- Searching / counting ---
3 in lst                    # membership test -- O(n)
lst.index(3)                 # index of first occurrence; raises ValueError if missing
lst.count(3)                 # number of occurrences
len(lst)                     # number of elements


# --- Ordering ---
lst.sort()                   # sort in place, ascending
lst.sort(reverse=True)        # sort in place, descending
lst.sort(key=len)             # sort in place using a key function
sorted(lst)                   # return a new sorted list, original untouched
lst.reverse()                 # reverse in place


# --- Copying ---
copy1 = lst.copy()            # shallow copy
copy2 = lst[:]                 # shallow copy via slicing
copy3 = list(lst)              # shallow copy via constructor


# --- Converting to other types ---
set(lst)                       # convert list to set -- drops duplicates, order not guaranteed
tuple(lst)                      # convert list to tuple
"".join(lst)                    # convert list of strings to a single string


# --- Combining / repeating ---
a = [1, 2]
b = [3, 4]
a + b                           # concatenate two lists into a new list
a * 3                           # repeat list contents 3 times


# --- Iteration ---
for item in lst:                    # iterate over elements
    pass

for i, item in enumerate(lst):      # with index
    pass


# --- Notes ---
# - Lists are ordered and mutable -- unlike sets, duplicates and order are preserved.
# - Methods like .append(), .sort(), .reverse(), .extend() mutate in place and return None --
#   don't do `lst = lst.append(x)`, that sets lst to None.
# - Functions like sorted(), list(), and slicing (lst[:]) return a NEW list instead of
#   mutating the original.
