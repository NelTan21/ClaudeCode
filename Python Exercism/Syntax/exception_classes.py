# exception_classes.py
# Reference sheet for Python's built-in exception class hierarchy


# --- Full hierarchy (indentation = inheritance) ---
"""
BaseException
 +-- BaseExceptionGroup
 +-- GeneratorExit
 +-- KeyboardInterrupt
 +-- SystemExit
 +-- Exception
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ExceptionGroup (subclass of BaseExceptionGroup and Exception)
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError (alias: IOError, EnvironmentError)
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- StopAsyncIteration
      +-- StopIteration
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- BytesWarning
           +-- DeprecationWarning
           +-- EncodingWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- PendingDeprecationWarning
           +-- ResourceWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UnicodeWarning
           +-- UserWarning
"""


# --- BaseException-level (rarely caught directly; usually let these propagate) ---
# BaseException          -- root of ALL exceptions; catching this catches everything
# BaseExceptionGroup      -- wraps multiple unrelated exceptions raised together (3.11+)
# GeneratorExit           -- raised inside a generator when it's closed via .close()
# KeyboardInterrupt       -- user pressed Ctrl+C
# SystemExit              -- raised by sys.exit()


# --- Exception (base class for almost everything you should actually catch) ---
# Exception               -- base class for all "normal" catchable errors


# --- ArithmeticError family ---
# ArithmeticError         -- base class for numeric errors
# FloatingPointError      -- floating point operation failed (rarely raised in practice)
# OverflowError           -- result of an arithmetic operation too large to represent
# ZeroDivisionError       -- division or modulo by zero (e.g. 1 / 0)


# --- Common standalone errors ---
# AssertionError          -- an `assert` statement's condition was False
# AttributeError          -- attribute/method doesn't exist on an object (obj.missing_attr)
# BufferError             -- buffer-related operation failed
# EOFError                -- input() hit end-of-file with no data read
# MemoryError             -- operation ran out of memory
# NotImplementedError     -- abstract method or unfinished code path was called (RuntimeError subclass)
# ReferenceError          -- weak reference's referent was garbage collected
# RuntimeError            -- generic "something went wrong" not covered elsewhere
# RecursionError          -- maximum recursion depth exceeded (RuntimeError subclass)
# SystemError             -- internal interpreter error (should not normally happen)
# TypeError               -- operation applied to an object of the wrong type (1 + "a")
# ValueError              -- right type, but an inappropriate value (int("abc"))


# --- ImportError family ---
# ImportError             -- an import statement failed
# ModuleNotFoundError     -- specifically, the module itself could not be found


# --- LookupError family ---
# LookupError             -- base class for invalid lookups
# IndexError              -- sequence index out of range ([1, 2, 3][10])
# KeyError                -- dict key not found (my_dict["missing"])


# --- NameError family ---
# NameError               -- name not found in local or global scope
# UnboundLocalError       -- local variable referenced before assignment


# --- OSError family (a.k.a. IOError / EnvironmentError -- these are aliases) ---
# OSError                 -- base class for system/OS-related errors
# BlockingIOError         -- operation would block on a non-blocking resource
# ChildProcessError       -- error related to a child process
# ConnectionError         -- base class for connection-related errors
# BrokenPipeError         -- write to a pipe/socket with no reader on the other end
# ConnectionAbortedError  -- connection attempt aborted by the peer
# ConnectionRefusedError  -- connection attempt refused by the peer
# ConnectionResetError    -- connection reset by the peer
# FileExistsError         -- trying to create a file/directory that already exists
# FileNotFoundError       -- file or directory does not exist
# InterruptedError        -- system call interrupted by a signal
# IsADirectoryError       -- file operation requested on a directory
# NotADirectoryError      -- directory operation requested on a non-directory
# PermissionError         -- insufficient permissions to perform the operation
# ProcessLookupError      -- process does not exist
# TimeoutError            -- system function timed out


# --- Iteration-related ---
# StopIteration           -- next() called on an exhausted iterator
# StopAsyncIteration      -- async equivalent of StopIteration


# --- Syntax-related (raised at parse/compile time, not typically caught at runtime) ---
# SyntaxError             -- invalid Python syntax
# IndentationError        -- incorrect indentation (SyntaxError subclass)
# TabError                -- inconsistent use of tabs and spaces (IndentationError subclass)


# --- Unicode-related (ValueError subclasses) ---
# UnicodeError            -- base class for encoding/decoding errors
# UnicodeDecodeError      -- decoding bytes to str failed
# UnicodeEncodeError      -- encoding str to bytes failed
# UnicodeTranslateError   -- translating str failed


# --- Warnings (not errors -- typically shown, not raised, unless filters escalate them) ---
# Warning                 -- base class for all warnings
# BytesWarning            -- issues related to bytes/bytearray usage
# DeprecationWarning      -- feature is deprecated (visible to developers)
# EncodingWarning         -- default encoding used when an explicit one was expected (3.10+)
# FutureWarning           -- feature will change behavior in the future (visible to end users)
# ImportWarning           -- issues related to module import
# PendingDeprecationWarning -- feature will be deprecated in the future
# ResourceWarning         -- issues related to resource usage/cleanup (e.g. unclosed file)
# RuntimeWarning          -- suspicious runtime behavior
# SyntaxWarning           -- suspicious syntax
# UnicodeWarning          -- issues related to Unicode handling
# UserWarning             -- default category for warnings.warn()


# --- Notes ---
# - Catch the MOST SPECIFIC exception that applies; only catch broad classes
#   (Exception, or worse, BaseException) when you genuinely want to handle
#   "anything at all", since that also swallows bugs you didn't anticipate.
# - Avoid catching BaseException directly in normal code -- it also covers
#   SystemExit and KeyboardInterrupt, which should almost always propagate.
# - You can inspect an exception's full ancestry at any time:
#       ValueError.__mro__
#   (mro = "method resolution order", i.e. the chain of parent classes)
