# My Answer
def remove_duplicates(spells):
    casted_spells = set()
    unique_spells = []
    for spell in spells:
        print(f"Learning Spell:({spell})...")
        if spell not in unique_spells:
            print(f"Adding New Spell:({spell})")
            unique_spells.append(spell)
            continue
        print(f"Spell:({spell}) already learned")
        casted_spells.add(spell)
        print(f"These are the casted spells:({casted_spells})")
    return unique_spells

# Solution
"""
def remove_duplicates(spells):
    seen = set()
    deduped_spells = []
    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            deduped_spells.append(spell)
    return deduped_spells


def alt_remove_duplicates(spells):
    return list(set(spells))
"""