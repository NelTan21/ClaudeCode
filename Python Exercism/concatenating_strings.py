def join_strings(strings: list[str]) -> str:
    joined_string = ""
    for string in range(0,len(strings)):
        if string < (len(strings) -1):
            joined_string += strings[string] + ","
        else:
            joined_string += strings[string]
    return joined_string

# Activity Solution
"""
def join_strings(strings: list[str]) -> str:
    joined = ""
    for s in strings:
        joined += s + ","
    return joined[:-1]
"""