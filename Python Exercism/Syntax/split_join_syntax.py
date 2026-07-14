# split_join_syntax.py
# Reference sheet for str.split() and str.join()


# --- split(): string -> list ---
text = "hello world foo"
text.split()                    # -> ['hello', 'world', 'foo']  (splits on any whitespace, drops extras)
text.split(" ")                  # -> ['hello', 'world', 'foo']  (splits on exact " ")

csv = "a,b,,c"
csv.split(",")                    # -> ['a', 'b', '', 'c']  (keeps empty strings between delimiters)

path = "a/b/c/d"
path.split("/")                    # -> ['a', 'b', 'c', 'd']
path.split("/", 1)                  # -> ['a', 'b/c/d']  (maxsplit=1 -- only split once, from the left)
path.rsplit("/", 1)                  # -> ['a/b/c', 'd']  (splits from the RIGHT instead)

lines = "line1\nline2\nline3"
lines.split("\n")                     # -> ['line1', 'line2', 'line3']
lines.splitlines()                      # -> ['line1', 'line2', 'line3']  (handles \n, \r\n, etc.)


# --- join(): list -> string ---
words = ["hello", "world", "foo"]
" ".join(words)                  # -> "hello world foo"   (separator string . join(iterable))
"-".join(words)                    # -> "hello-world-foo"
"".join(words)                       # -> "helloworldfoo"  (no separator)
",".join(["1", "2", "3"])              # -> "1,2,3"  -- items must ALL be strings already

nums = [1, 2, 3]
",".join(str(n) for n in nums)          # -> "1,2,3"  -- convert to str first (join needs strings)
",".join(map(str, nums))                  # same result, alternate style


# --- round trip: split then join (or vice versa) ---
sentence = "the quick brown fox"
words = sentence.split()             # -> ['the', 'quick', 'brown', 'fox']
rebuilt = " ".join(words)              # -> "the quick brown fox"  (back to original)


# --- Notes ---
# - split() is a STRING method that returns a list.
# - join() is also a STRING method (the separator), but it's called ON the separator,
#   with the iterable passed as the argument -- separator.join(iterable), not iterable.join(separator).
# - join() requires every element to already be a string, or it raises a TypeError --
#   use str(x) or map(str, iterable) to convert numbers first.
# - text.split() with no argument also strips leading/trailing whitespace and collapses
#   multiple spaces; text.split(" ") does NOT -- it treats every single space as a delimiter.
