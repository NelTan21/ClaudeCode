# type_hints_syntax.py
# Reference sheet for Python type hints (annotations)
# NOTE: type hints are NOT enforced at runtime -- Python ignores them during
# execution. They exist purely for readability and for external tools
# (IDEs, mypy, pyright) to catch mistakes before you run the code.


# --- Basic variable annotations ---
age: int = 25
name: str = "Slayer"
level: float = 4.5
is_active: bool = True


# --- Function parameter and return type hints ---
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def print_message(message: str) -> None:   # -> None means the function returns nothing
    print(message)


# --- Default values combined with hints ---
def get_player(player_id: int = 0) -> str:
    return f"player {player_id}"


# --- Built-in collection hints ---
def total_score(scores: list[int]) -> int:      # list of ints           (Python 3.9+)
    return sum(scores)

def get_names() -> tuple[str, str]:               # tuple of exactly two strings
    return ("Slayer", "Dorgoth")

def unique_ids(ids: set[int]) -> set[int]:          # set of ints
    return ids

def player_levels() -> dict[str, int]:                # dict[key_type, value_type]
    return {"Slayer": 128, "Dorgoth": 300}


# --- Older syntax for collections (pre-3.9, still common in older code/tutorials) ---
from typing import List, Tuple, Set, Dict

def total_score_old(scores: List[int]) -> int:
    return sum(scores)

def player_levels_old() -> Dict[str, int]:
    return {"Slayer": 128}


# --- Optional -- value can be the given type OR None ---
from typing import Optional

def find_player(player_id: int) -> Optional[str]:    # same as: str | None
    return None

def find_player_new(player_id: int) -> str | None:     # modern syntax (Python 3.10+)
    return None


# --- Union -- value can be one of several types ---
from typing import Union

def parse_score(score: Union[int, str]) -> int:      # int OR str
    return int(score)

def parse_score_new(score: int | str) -> int:          # modern syntax (Python 3.10+)
    return int(score)


# --- Any -- explicitly "could be anything" (turns off type checking for that value) ---
from typing import Any

def process(data: Any) -> Any:
    return data


# --- Callable -- hints for functions passed as arguments ---
from typing import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))
    # Callable[[int], int] means: a function that takes one int and returns an int


# --- Type aliases -- give a complex type hint a readable name ---
PlayerRecord = dict[str, int]

def get_record() -> PlayerRecord:
    return {"level": 128}


# --- Class attribute hints ---
class Player:
    name: str
    level: int

    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level


# --- Checking hints at runtime (rarely needed, but available) ---
def show_hints(func) -> None:
    print(func.__annotations__)      # dict of {param_name: type, "return": type}

show_hints(add)     # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


# --- Notes ---
# - Type hints are NOT enforced by Python itself -- this runs with no error
#   even though it violates the hint:
#       def add(a: int, b: int) -> int:
#           return a + b
#       add("x", "y")     # returns "xy", no TypeError raised by the hint
# - Enforcement only happens if you run a separate static type checker,
#   such as mypy or pyright, against your code.
# - Prefer the modern `X | None` / `X | Y` syntax (3.10+) over
#   `Optional[X]` / `Union[X, Y]` in new code -- functionally identical,
#   just less to import.
# - list[int], dict[str, int], etc. (lowercase builtins) work directly as
#   hints since Python 3.9 -- no import needed. Older code often imports
#   List, Dict, Tuple, Set from `typing` instead.
