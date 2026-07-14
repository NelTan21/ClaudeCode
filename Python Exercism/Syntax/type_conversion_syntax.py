# type_conversion_syntax.py
# Reference sheet for converting between data types in Python


# --- Converting to int ---
int("42")                    # 42          -- string of digits -> int
int("42", 2)                  # 2           -- parse string as base 2 (binary)
int("2A", 16)                   # 42          -- parse string as base 16 (hex)
int(3.99)                        # 3           -- float -> int TRUNCATES (does not round)
int(-3.99)                        # -3          -- truncates toward zero, not down
int(True)                          # 1           -- bool -> int
int(False)                          # 0
# int("3.14")                        # ValueError -- can't parse a decimal string directly
# int("abc")                           # ValueError -- not a valid number


# --- Converting to float ---
float("3.14")                 # 3.14        -- string -> float
float("42")                    # 42.0        -- int-looking string also works
float(42)                        # 42.0        -- int -> float
float(True)                       # 1.0
float("inf")                       # inf         -- special float values
float("-inf")                       # -inf
# float("abc")                          # ValueError


# --- Converting to str ---
str(42)                        # "42"        -- int -> str
str(3.14)                       # "3.14"      -- float -> str
str(True)                        # "True"      -- bool -> str
str([1, 2, 3])                     # "[1, 2, 3]" -- list -> its printable representation
str(None)                           # "None"
f"{42}"                              # "42"        -- f-string is another common way to stringify


# --- Converting to bool ---
bool(0)                        # False       -- 0 is falsy
bool(1)                         # True        -- any nonzero number is truthy
bool(-1)                         # True        -- negative numbers are ALSO truthy
bool("")                           # False       -- empty string is falsy
bool("False")                       # True        -- non-empty string is ALWAYS truthy, even this one!
bool([])                              # False       -- empty list is falsy
bool([0])                              # True        -- non-empty list is truthy, even if it contains falsy items
bool(None)                              # False


# --- Converting between collection types ---
list("abc")                    # ['a', 'b', 'c']      -- string -> list of characters
list((1, 2, 3))                  # [1, 2, 3]              -- tuple -> list
list({1, 2, 3})                    # [1, 2, 3]                -- set -> list (order not guaranteed)
list({"a": 1, "b": 2})               # ['a', 'b']                 -- dict -> list of its KEYS

tuple([1, 2, 3])                # (1, 2, 3)     -- list -> tuple
tuple("abc")                      # ('a', 'b', 'c')

set([1, 1, 2, 2, 3])              # {1, 2, 3}     -- list -> set (drops duplicates)
set("aabbcc")                       # {'a', 'b', 'c'}

dict([("a", 1), ("b", 2)])            # {'a': 1, 'b': 2}    -- list of 2-item pairs -> dict
dict(zip(["a", "b"], [1, 2]))           # {'a': 1, 'b': 2}    -- zip two lists into a dict


# --- String <-> list of characters/words ---
list("hello")                    # ['h', 'e', 'l', 'l', 'o']
"".join(["h", "e", "l", "l", "o"])  # "hello"        -- list of chars -> string
"a,b,c".split(",")                    # ['a', 'b', 'c']  -- string -> list, split on delimiter
",".join(["a", "b", "c"])                # "a,b,c"          -- list -> string, joined with delimiter


# --- Numeric base conversions (int -> string in another base) ---
bin(10)                         # '0b1010'     -- int -> binary string
oct(10)                          # '0o12'        -- int -> octal string
hex(10)                            # '0xa'         -- int -> hexadecimal string
int('0b1010', 0)                     # 10            -- auto-detect base from prefix
int('0xa', 0)                          # 10


# --- Character <-> code point ---
ord("A")                        # 65            -- character -> Unicode code point
chr(65)                          # "A"           -- Unicode code point -> character


# --- Rounding vs truncating (both return different types depending on args) ---
round(3.7)                      # 4    (int)     -- rounds to nearest whole number
round(3.14159, 2)                 # 3.14 (float)   -- rounds to N decimal places
int(3.7)                            # 3    (int)     -- truncates instead of rounding


# --- bytes <-> str ---
"hello".encode()                 # b'hello'      -- str -> bytes
b"hello".decode()                  # "hello"       -- bytes -> str
"hello".encode("utf-8")               # b'hello'      -- explicit encoding


# --- Notes ---
# - int(float) TRUNCATES toward zero; it does not round. Use round() if you want
#   normal rounding behavior.
# - Almost anything non-empty/nonzero is "truthy" when converted with bool() --
#   including the string "False", which is famously a common bug source.
# - dict(list_of_pairs) expects each item to be a 2-element pair (tuple/list);
#   anything else raises a ValueError.
# - Converting a dict directly (list(some_dict)) gives you its KEYS, not its
#   values or key-value pairs -- use .values() or .items() for those.
