# Classes - stores name-value pairs
    # Defines a new class called "Soldier"
    # with three properties: health, armor, damage
class Soldier:
    health: int = 5
    armor: int = 3
    damage: int = 2

# Objects - instances of a class.
health = 50         # health is an instance of an integer type
aragorn = Soldier()  # aragorn is an instance of the Soldier class type

# Example interaction of Class and Objects:
class Archer:
    health: int = 40
    arrows: int = 10
# Create several instances of the Archer class
legolas = Archer()
bard = Archer()
# Print class properties
print(legolas.health) # 40
print(bard.arrows) # 10