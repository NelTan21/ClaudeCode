# Classes - stores name-value pairs 
    # Defines a new class called "Soldier"
    # with three properties: health, armor, damage(attributes)
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

# ---------------------------------------------------------------------------
# self / __init__ - self is the instance currently being worked with.
# __init__ runs automatically when a class is called (instantiated),
# and self.attribute = value attaches that value onto THAT instance only.
class Archer:
    def __init__(self, health, arrows):
        self.health = health
        self.arrows = arrows

    def shoot(self):
        self.arrows -= 1
        print(f"Twang! {self.arrows} arrows left.")

legolas = Archer(40, 10)
bard = Archer(35, 8)

legolas.shoot()      # Twang! 9 arrows left.
print(bard.arrows)   # 8 - unaffected, each instance holds its own data

# Instances - objects created from a class blueprint.
# Instantiation - the act of creating an instance (calling ClassName()).
# Attributes - the name-value pairs (health, arrows) a class defines and
#   an instance holds its own copy of.
# Example - legolas.health and legolas.arrows are attributes that belong
#   to the instance "legolas", instantiated from the Archer class.

# ---------------------------------------------------------------------------
# Inheritance - a subclass reuses (inherits) attributes and methods from
# its parent (base) class, and can add or override its own.
class Elf(Archer):                        # Elf inherits from Archer
    def __init__(self, health, arrows, stealth):
        super().__init__(health, arrows)  # reuse Archer's __init__ for health/arrows
        self.stealth = stealth            # new attribute, only Elf has this

    def shoot(self):                      # override - replaces Archer.shoot for Elf
        super().shoot()                   # optional: still run Archer's version first
        print("...you never even saw it coming.")

legolas = Elf(40, 10, 9)

print(legolas.health)               # 40  <- inherited from Archer
print(legolas.arrows)               # 10  <- inherited from Archer
print(legolas.stealth)              # 9   <- defined only on Elf
print(isinstance(legolas, Archer))  # True - an Elf IS-A Archer

# Polymorphism - same method name, different behavior depending on
# which class the instance actually is.
bard.shoot()      # Archer.shoot() -> "Twang! 7 arrows left."
legolas.shoot()   # Elf.shoot()    -> "Twang! 9 arrows left." + the extra line

# ---------------------------------------------------------------------------
# Method - they are functions that live inside classes
# Methods do not require return values as they mutate the attributes inherited by the object
# Key indicator that a return value is not expected from a method
    # There is no variable catching for results (results = object.method())
    # There is no print statement to stdout outputs (print(object.method())
    # The self parameter is mutated within the method being called def method(self): (self.something = something)

# ---------------------------------------------------------------------------
# Constructor - Creates an initialization file for the Object that takes in arguments from the Instance parameters
    # This is a method that is being called everytime an Instantiation happens
    # Method syntax <def __init__(self, arg1, arg2...)>
class Archer:
    def __init__(self, name:str, health:int, num_arrows:int)-> None:
        self.name: str = name
        self.health: int = health
        self.num_arrows: int = num_arrows

# ---------------------------------------------------------------------------
## Class Variables vs. Instance Variables          
    # Class Variables - does not use a constructor so attributes are shared across instances
    # Instance Variables - Uses a constructor so attributes varies depending on arguments declared upon Instantiation  Class Variables vs. Instance Variables          
    # Class Variables - does not use a constructor so initial attributes are shared across instances upon Instantiation
    # Instance Variables - Uses a constructor so attributes varies depending on arguments declared upon Instantiation

# ---------------------------------------------------------------------------
# General OOP Principle:
# Prefer holding onto the object itself rather than extracting pieces of it into a separate structure
# Only transform objects for specific reasons (like needing something hashable, or serializing for storage).  

# ---------------------------------------------------------------------------
# Encapsulation - The practice of hiding complexity in a black box or creating your "under the hood"
# Encapsulation and the concepts of private and public members have NOTHING to do with security. This really confused me as a new developer. Just as the casing on your computer hides its inner workings but doesn't stop you from opening the case and looking inside, encapsulation doesn't stop anyone from knowing how your code works, it just puts it all in one easy to find place.
acceleration: float = calc_acceleration(initial_speed, final_speed, time)
    # in order to calculate for acceleration, we dont need to know the methods...
    # We just need to know the inputs required to calculate for it.

# Public - by default all properties and methods in a Class are public, you can access them with a .
wall.height = 10
print(wall.height)
# 10
# Private - You can encapsulate logic and data within a class by prefixing with 2 underscores __
    # You can create method that you can call outside the class to produce private data
    # You cant directly print/return/read private attributes outside the class
class Wall:
    def __init__(self, armor: int, magic_resistance: int) -> None:
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self) -> int:
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30

# ---------------------------------------------------------------------------
#class BankAccount:
    def __init__(self, account_number: str, initial_balance: float) -> None:
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self) -> str:
        return self.__account_number

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0.00:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0.00:
            raise ValueError("cannot withdraw zero or negative funds")
        elif self.__balance < amount:
            raise ValueError("insufficient funds")
        self.__balance -= amount Abstraction - Similar to encapsulation but differs on how it is worked with.
# Abstraction works towards how the product is presented. Reduces what the caller needs to know.
# Encapsulation works towards how the product is handled. Reduces what the caller needs to touch.
