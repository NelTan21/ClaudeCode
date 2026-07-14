# delete_syntax.py
# Reference sheet for deleting/removing elements across different Python types
# (See list_syntax.py / dictionary_syntax.py / set_syntax.py for full details on each type)


# --- list: removing elements ---
lst = [1, 2, 3, 4]
lst.remove(3)                 # remove first occurrence of a VALUE; raises ValueError if missing
lst.pop()                      # remove and return LAST element
lst.pop(0)                      # remove and return element at INDEX 0
del lst[0]                       # delete element at index 0 (no return value)
del lst[1:3]                      # delete a slice
lst.clear()                        # remove all elements -- same object, now empty


# --- dict: removing entries ---
d = {"a": 1, "b": 2, "c": 3}
del d["a"]                     # delete key; raises KeyError if missing
d.pop("b")                       # remove and return value; raises KeyError if missing
d.pop("z", None)                   # remove and return value, default if missing (no error)
d.popitem()                          # remove and return the LAST inserted (key, value) pair
d.clear()                              # remove all entries


# --- set: removing elements ---
s = {1, 2, 3}
s.remove(2)                    # remove element; raises KeyError if missing
s.discard(99)                    # remove element if present; NO error if missing
s.pop()                            # remove and return an ARBITRARY element (sets are unordered)
s.clear()                            # remove all elements


# --- string / tuple: "deleting" (immutable -- must build a new one) ---
text = "hello world"
text = text.replace("world", "")   # -> "hello " (new string, target removed)
text = text[:5]                      # slicing off the rest (new string)

t = (1, 2, 3)
t = t[:1] + t[2:]                       # drop index 1 -- (1, 3) -- new tuple


# --- deleting a variable itself ---
x = 5
del x                            # removes the NAME entirely -- using x after this raises NameError


# --- safely removing while iterating ---
lst = [1, 2, 3, 4, 5]
for item in lst[:]:              # iterate over a COPY so mutating lst is safe
    if item % 2 == 0:
        lst.remove(item)


# --- Notes ---
# - remove()/del/pop() on a MISSING value or index raises an error (ValueError/KeyError/IndexError).
#   Use discard() (sets) or pop(key, default) (dicts) when "missing is fine."
# - pop() returns the removed item; del and remove()/discard() do not.
# - Never remove()/pop()/del from a list while iterating over the ORIGINAL list --
#   indices shift and elements get skipped. Iterate a copy (lst[:]) or filter into a new list.
# - Immutable types (str, tuple) can't delete in place -- any "delete" builds a new object.
