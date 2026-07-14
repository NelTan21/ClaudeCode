# add_syntax.py
# Reference sheet for adding elements across different Python types
# (See list_syntax.py / dictionary_syntax.py / set_syntax.py for full details on each type)


# --- list: adding elements ---
lst = [1, 2, 3]
lst.append(4)                 # add single element to the end
lst.insert(0, 99)              # insert element at a specific index
lst.extend([5, 6])             # append multiple elements from an iterable
lst += [7, 8]                   # same effect as extend
lst = lst + [9]                  # concatenation -- returns a NEW list


# --- dict: adding entries ---
d = {"a": 1}
d["b"] = 2                      # add new key (or overwrite if it exists)
d.setdefault("c", 0)              # adds key only if missing, returns its value
d.update({"d": 4})                 # add/merge multiple keys at once
d |= {"e": 5}                        # merge operator (Python 3.9+)


# --- set: adding elements ---
s = {1, 2, 3}
s.add(4)                         # add single element (no-op if already present)
s.update([5, 6])                   # add multiple elements from an iterable
s |= {7, 8}                          # union-update operator, same as .update()


# --- string: "adding" (strings are immutable -- always creates a new string) ---
text = "hello"
text += " world"                  # concatenation -- creates a new string
text = text + "!"                   # same idea
parts = ["a", "b", "c"]
joined = "-".join(parts)             # "a-b-c" -- build a string from pieces


# --- tuple: "adding" (tuples are immutable -- must build a new tuple) ---
t = (1, 2)
t = t + (3,)                       # concatenation -- creates a new tuple, note the trailing comma


# --- Notes ---
# - Mutable types (list, dict, set) can add in place: .append/.insert/.extend, [key]=,
#   .setdefault/.update, .add/.update.
# - Immutable types (str, tuple) can never be modified in place -- any "add" operation
#   actually builds and returns a brand new object.
# - list.append() adds ONE element (even if it's a list -- it gets nested);
#   list.extend() adds each element FROM an iterable individually.
