def calculate_damage(sword, arrow, spear, dagger, fireball):
    """
    Calculates the total and average damage across five weapon types.

    Args:
        sword (int): Damage dealt by the sword.
        arrow (int): Damage dealt by the arrow.
        spear (int): Damage dealt by the spear.
        dagger (int): Damage dealt by the dagger.
        fireball (int): Damage dealt by the fireball.

    Returns:
        tuple: (total_damage, average_damage)
    """
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage

def debug_calculate_damage(sword, arrow, spear, dagger, fireball):
    total, avg = calculate_damage(sword, arrow, spear, dagger, fireball)
    print(f"Damage Taken:\nSword:\t\t{sword}\nArrow:\t\t{arrow}\nSpear:\t\t{spear}\nDagger:\t\t{dagger}\nFireball:\t{fireball}\n--------\t--------\nTotal:\t\t{total}\nAverage:\t{avg}")

debug_calculate_damage(5,5,5,5,5)