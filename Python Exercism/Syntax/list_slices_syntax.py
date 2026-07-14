s = [10, 20, 30, 40, 50]

s[1:4]    # [20, 30, 40]
s[:3]     # [10, 20, 30]
s[2:]     # [30, 40, 50]
s[:]      # whole copy
s[::2]    # [10, 30, 50]
s[::-1]   # reversed

"""
Rules:

start = where to begin
stop = where to stop before
step = how to move
omitted values use defaults
Useful notes:

stop is exclusive
negative indices count from the end
negative step goes backward
Examples with negatives:
"""

s[-1]     # 50
s[-3:]    # [30, 40, 50]
s[:-1]    # [10, 20, 30, 40]
s[::-1]   # [50, 40, 30, 20, 10]