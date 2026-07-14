def get_heroes():
    heroes = [
        "Glorfindel",
        2093,
        True,
        "Gandalf",
        1054,
        False,
        "Gimli",
        389,
        False,
        "Aragorn",
        87,
        # True <- Commented to simulate a what if on missing data at the end
    ]
    updated_heroes = []
    while heroes:
        if len(heroes) > 2:
            updated_heroes.append((heroes.pop(0), heroes.pop(0), heroes.pop(0)))
            continue
        elif len(heroes) > 1:
            updated_heroes.append((heroes.pop(0), heroes.pop(0),None))
            continue
        updated_heroes.append((heroes.pop(),None,None))    
    return updated_heroes

"""    updated_heroes = []
    for i in range(0, len(heroes),3):
        updated_heroes.append((heroes[i], heroes[i+1], heroes[i+2]))
    return updated_heroes
"""