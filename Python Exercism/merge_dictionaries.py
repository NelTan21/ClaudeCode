def merge(dict1, dict2):
    merged_guild = {}
    print(f"This is dict1 {dict1}")
    print(f"This is dict2 {dict2}")
    for key in dict1:
        print(f"This is the key:({key})")
        level = dict1[key]
        print(f"This is the level:({level})")
        merged_guild[key] = level
        print(f"This is the merged result after dict1{merged_guild}")
        continue
    for key in dict2:
        print(f"This is the key:({key})")
        level = dict2[key]
        print(f"This is the level:({level})")
        merged_guild[key] = level
        print(f"This is the merged result after dict1{merged_guild}")
        continue
    print(f"This is the final merged result {merged_guild}")
    return merged_guild