# try_syntax.py
# Reference sheet for Python try/except syntax and error handling


# --- Basic try/except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")


# --- Catching multiple exception types separately ---
try:
    result = int("abc")
except ValueError:
    print("Invalid value")
except TypeError:
    print("Invalid type")


# --- Catching multiple exception types together ---
try:
    result = int("abc")
except (ValueError, TypeError):
    print("Invalid value or type")


# --- Accessing the exception object ---
try:
    result = int("abc")
except ValueError as e:
    print(f"Error occurred: {e}")


# --- Catching any exception (use sparingly -- hides unrelated bugs) ---
try:
    risky_call()
except Exception as e:
    print(f"Something went wrong: {e}")


# --- Bare except (catches everything, including KeyboardInterrupt/SystemExit --
#     almost always avoid this in real code) ---
try:
    risky_call()
except:
    print("An error occurred")


# --- else: runs only if the try block did NOT raise ---
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print(f"Success: {result}")


# --- finally: always runs, whether an exception occurred or not ---
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Cleanup runs no matter what")


# --- Full structure: try / except / else / finally ---
try:
    value = int("42")
except ValueError:
    print("Conversion failed")
else:
    print(f"Conversion succeeded: {value}")
finally:
    print("Done attempting conversion")


# --- Raising exceptions ---
raise ValueError("Something is wrong")          # raise a new exception
raise ValueError("Something is wrong") from e    # raise while chaining the original cause


# --- Re-raising the caught exception (inside an except block) ---
try:
    risky_call()
except Exception:
    print("Logging error before re-raising")
    raise                        # re-raises the same exception, preserving traceback


# --- Custom exceptions ---
class SpellNotFoundError(Exception):
    pass

try:
    raise SpellNotFoundError("fireball is not a known spell")
except SpellNotFoundError as e:
    print(f"Custom error: {e}")


# --- assert (raises AssertionError if condition is False) ---
assert 1 + 1 == 2
assert 1 + 1 == 2, "Math is broken"    # optional custom error message


# --- Common built-in exception types ---
# ValueError          -- right type, inappropriate value (int("abc"))
# TypeError           -- wrong type used in an operation (1 + "a")
# KeyError            -- missing dict key
# IndexError          -- list/sequence index out of range
# AttributeError      -- attribute/method doesn't exist on object
# ZeroDivisionError   -- division or modulo by zero
# FileNotFoundError   -- file/path doesn't exist
# StopIteration       -- next() called on exhausted iterator
# ImportError / ModuleNotFoundError -- import failed


# --- Notes ---
# - `except` clauses are checked top-to-bottom; put more specific exception types
#   before more general ones (e.g. ValueError before Exception).
# - `else` only runs if no exception was raised -- useful for code that should run
#   only on success, kept separate from the try block being "protected".
# - `finally` always runs -- even if the try/except block returns or re-raises --
#   commonly used for cleanup (closing files, releasing locks).
# - Avoid bare `except:` -- it also catches KeyboardInterrupt and SystemExit,
#   which usually should not be swallowed.
