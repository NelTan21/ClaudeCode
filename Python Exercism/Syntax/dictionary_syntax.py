# Dictionary Syntax reference
# Run this file to see each form of dict syntax in action.

# --- Creating dicts ---
d = {}                                   # empty dict
d = dict()                                # empty dict (alt)
d = {"a": 1, "b": 2}                       # literal
d = dict(a=1, b=2)                          # keyword args (keys must be valid identifiers)
d = dict([("a", 1), ("b", 2)])               # from list of pairs
d = dict(zip(["a", "b"], [1, 2]))             # from two parallel lists
d = dict.fromkeys(["a", "b"], 0)               # {"a": 0, "b": 0}
d = {k: v for k, v in [("a", 1), ("b", 2)]}     # dict comprehension
d = {k: v for k, v in [("a", 1), ("b", 2)] if v > 0}  # comprehension with filter
print("creation:", d)

# --- Accessing values ---
d = {"a": 1, "b": 2}
print(d["a"])                # raises KeyError if missing
print(d.get("a"))             # None if missing
print(d.get("z", 0))           # 0 if missing (default)
print(d.setdefault("z", 0))     # returns d["z"] if present, else sets and returns 0
print("after setdefault:", d)

# --- Adding / updating ---
d["c"] = 3                     # add or overwrite single key
d.update({"a": 10, "d": 4})     # merge in another dict
d.update(e=5, f=6)               # merge via keyword args
d.update([("g", 7)])              # merge via pairs
d |= {"h": 8}                       # merge operator (Python 3.9+, in-place)
d2 = d | {"i": 9}                     # merge operator, returns new dict (3.9+)
print("after updates:", d)
print("merged copy:", d2)

# --- Removing ---
d3 = {"a": 1, "b": 2, "c": 3}
del d3["a"]                    # raises KeyError if missing
popped = d3.pop("b")             # removes and returns value, raises KeyError if missing
popped_default = d3.pop("z", None)  # removes and returns value, default if missing
last_item = d3.popitem()          # removes and returns last inserted (key, value) pair
print("after removals:", d3, popped, popped_default, last_item)
d3.clear()                          # empties the dict
print("after clear:", d3)

# --- Checking membership ---
d = {"a": 1, "b": 2}
print("a" in d)              # checks keys
print("a" not in d)
print(1 in d.values())        # checks values

# --- Iterating ---
for k in d:                 # keys (default)
    pass
for k in d.keys():            # keys explicit
    pass
for v in d.values():           # values
    pass
for k, v in d.items():          # key-value pairs
    pass

# --- Views / conversions ---
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
print(len(d))

# --- Copying ---
d_copy = d.copy()               # shallow copy
d_copy2 = dict(d)                 # shallow copy (alt)
import copy
d_deep = copy.deepcopy(d)           # deep copy

# --- Unpacking ---
def f(**kwargs):
    print(kwargs)

f(**d)                          # unpack as keyword arguments
merged = {**d, **{"c": 3}}        # merge via unpacking (later keys win)
merged2 = {**d, "x": 1}             # unpack + add/override
print(merged, merged2)

# --- Comparisons ---
print({"a": 1, "b": 2} == {"b": 2, "a": 1})   # True: same keys/values, order-independent

# --- Nested / default patterns ---
from collections import defaultdict
dd = defaultdict(list)           # missing keys auto-create empty list
dd["x"].append(1)
di = defaultdict(int)              # missing keys auto-create 0
di["y"] += 1
print(dd, di)

from collections import Counter
c = Counter(["a", "b", "a"])         # {"a": 2, "b": 1}
print(c)

# from collections import OrderedDict  # rarely needed now (dicts are ordered since 3.7)

# --- Pattern matching (Python 3.10+) ---
sample = {"a": 1, "b": 2, "c": 3}
match sample:
    case {"a": 1, **rest}:
        print("matched, rest =", rest)
