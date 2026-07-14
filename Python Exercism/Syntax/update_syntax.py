# update_syntax.py
# Reference sheet for updating/replacing existing elements across different Python types
# (See list_syntax.py / dictionary_syntax.py / set_syntax.py for full details on each type)


# --- list: updating elements ---
lst = [1, 2, 3]
lst[0] = 99                     # replace element at index 0
lst[1:3] = [7, 8]                 # replace a slice with new values (lengths don't need to match)
lst[:] = [x * 2 for x in lst]       # replace ALL contents in place (keeps same list object/id)


# --- dict: updating values ---
d = {"a": 1, "b": 2}
d["a"] = 10                      # overwrite existing key's value (same syntax as adding)
d.update({"a": 100, "c": 3})       # overwrite multiple keys, adds new ones too
d.update(a=1000)                     # overwrite via keyword args
d |= {"a": 10000}                      # merge operator, overwrites matching keys (3.9+)


# --- set: updating (sets have no index/keys -- "update" means merge in new elements) ---
s = {1, 2, 3}
s.update([3, 4, 5])               # adds new elements, duplicates ignored -- {1,2,3,4,5}
s |= {6, 7}                         # same idea via operator


# --- string: "updating" (immutable -- always produces a new string) ---
text = "hello world"
text = text.replace("world", "there")  # -> "hello there" (new string)
text = text[:5] + " python"              # slice + concat to "replace" a portion


# --- nested structures: updating in place ---
data = {"users": [{"name": "Alice", "age": 30}]}
data["users"][0]["age"] = 31        # drill into nested dict/list, then assign


# --- Notes ---
# - "Updating" a mutable type (list, dict, set) changes the object in place --
#   the variable's identity (id()) stays the same.
# - "Updating" an immutable type (str, tuple, int, float) can't happen --
#   you're really reassigning the variable to point at a brand new object.
# - dict[key] = value and d.update(...) do the same job: SET if new, OVERWRITE if existing.
#   There's no separate "add-only" or "update-only" dict syntax by default --
#   use d.setdefault(key, value) if you want add-only (won't overwrite existing).
