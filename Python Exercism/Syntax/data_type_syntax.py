# data_type_syntax.py
# Reference sheet for identifying and checking data types in Python


# --- type() -- get the exact type of a value ---
type(42)                    # <class 'int'>
type(3.14)                  # <class 'float'>
type("hello")                # <class 'str'>
type(True)                   # <class 'bool'>
type([1, 2, 3])               # <class 'list'>
type((1, 2, 3))                # <class 'tuple'>
type({1, 2, 3})                 # <class 'set'>
type({"a": 1})                   # <class 'dict'>
type(None)                        # <class 'NoneType'>
type(lambda: None)                 # <class 'function'>


# --- Comparing types directly ---
type(42) == int              # True
type(42) is int               # True -- preferred over == for type comparison (types are singletons)


# --- isinstance() -- check if a value IS an instance of a type (preferred way) ---
isinstance(42, int)             # True
isinstance(3.14, float)          # True
isinstance("hi", str)             # True
isinstance([1, 2], list)           # True
isinstance(True, bool)              # True
isinstance(True, int)                # True -- bool is a subclass of int!

# isinstance accepts a tuple of types -- checks if it matches ANY of them
isinstance(42, (int, float))          # True
isinstance("hi", (int, float))         # False


# --- Why isinstance() is usually better than type() == ---
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
type(d) == Animal                # False -- exact type only, ignores inheritance
isinstance(d, Animal)             # True  -- respects inheritance (Dog IS an Animal)


# --- issubclass() -- check class inheritance relationships directly ---
issubclass(Dog, Animal)            # True
issubclass(bool, int)               # True -- confirms bool inherits from int
issubclass(int, object)              # True -- everything inherits from object eventually


# --- callable() -- check if something can be called like a function ---
callable(print)                       # True
callable(len)                          # True
callable(42)                            # False
callable(lambda: None)                   # True


# --- hasattr() -- check if an object has a given attribute/method ---
hasattr("hello", "upper")                 # True -- str has .upper()
hasattr(42, "upper")                       # False -- int has no .upper()


# --- Checking for None specifically ---
x = None
x is None                                   # True -- preferred over x == None
x is not None                                # True/False


# --- Common built-in type names (as used with type()/isinstance()) ---
# int          -- whole numbers          (42)
# float        -- decimal numbers         (3.14)
# complex      -- complex numbers          (2 + 3j)
# bool         -- True / False              (subclass of int)
# str          -- text                       ("hello")
# list         -- ordered, mutable             ([1, 2, 3])
# tuple        -- ordered, immutable            ((1, 2, 3))
# set          -- unordered, unique, mutable      ({1, 2, 3})
# frozenset    -- unordered, unique, immutable      (frozenset([1, 2]))
# dict         -- key-value mapping                  ({"a": 1})
# NoneType     -- the type of None                     (only instance is None)
# function     -- def / lambda                           (def f(): pass)
# type         -- the type of a class itself               (type(int) is type)


# --- Checking numeric-ness / string-ness of string content ---
"123".isdigit()               # True  -- all characters are digits
"12.3".isdigit()               # False -- '.' is not a digit
"abc".isalpha()                  # True -- all characters are letters
"abc123".isalnum()                # True -- all characters are letters or digits
"   ".isspace()                     # True -- all characters are whitespace
"Hello".istitle()                     # True -- title-cased
"HELLO".isupper()                      # True
"hello".islower()                       # True


# --- Duck-typing style check (try/except instead of isinstance) ---
def is_number_like(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

is_number_like("3.14")     # True
is_number_like("abc")       # False


# --- Notes ---
# - Use isinstance() over type() == for almost all real code -- it respects
#   inheritance, so subclasses are correctly recognized as their parent type.
# - bool is technically a subclass of int (True == 1, False == 0) -- keep this
#   in mind if you ever need to distinguish actual booleans from integers.
# - Prefer `is None` / `is not None` over `== None` -- None is a singleton,
#   and `is` checks identity rather than relying on __eq__.
