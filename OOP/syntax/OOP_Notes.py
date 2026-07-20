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

# ---------------------------------------------------------------------------
# Classes in object-oriented programming are all about grouping data and behavior in one place: an object.
# Functional programmers tend to think of their code as inputs and outputs, and how those inputs and outputs transition the world from one state to the next

# ---------------------------------------------------------------------------
# Inheritance - Allows propagation of constructors and methods from a reference/parent class
# These inherits allows for more fine-tuned downstream models of a class
class Aircraft: #Parent Class
    def __init__(self, height: int, speed: int) -> None:
        self.__height = height # Private Attribute -> needs a getter method as done below
        self.speed = speed # Public Attribute -> accessible by the inheritors within their own class

    def fly_up(self) -> None:
        self.__height += self.speed
# Its good practice to have a getter method for each defined attribute of your parent class
# This is so that your inheritors have a method to call for the attributes inherited from the parent
    def get_height(self):
        return self.height

# In most cases for practicality and practice of proper encapsulation, your attributes should be private
# Below is the sample of the getter method in the event that the speed attribute becomes private
# A getter method is useful because private attributes are prefixed with two underscores __
# These 2 underscores trigger a name-mangling behavior in python
# Name-Mangling example: Helicopter calling self.__height would call it as _Helicopter__height instead
# You will encounter the nasty error of _Helicopter__height attribute does not exist

    # def get_speed(self):
        # return self.speed


class Helicopter(Aircraft): # Child Class Referencing the parent in enclosed parenthesis
    def __init__(self, height: int, speed: int) -> None:
        super().__init__(height, speed) # super() method returns a referenced constructor or method
        self.direction = 0

    def rotate(self) -> None:
        self.direction += 90
# A good child class is like a specific sub-category of the parent class
# Tiger inherits from Feline inherits from Animal inherits from LivingThing.


# Sometimes you can create blank Parent methods: only contains a "Pass"
# It serves as an guide that every subclass inheriting from the parent should create the same method.
# This is normally done if each subclass solves for the same thing but each uses a different calculation.
    # See: ../activities/inheritance_siege.py


# Inheritance can be classified into two types, Wide(Lateral) or Deep(Heirarchal)
# Learn to use both as each has their own tradeoffs but the most commonly used is Wide

# ---------------------------------------------------------------------------
# Wide (Lateral) Inheritance - several sibling classes inherit directly from
# ONE parent. The hierarchy stays flat (1 level deep), siblings don't inherit
# from each other.
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} is eating.")

class Feline(Animal):      # sibling
    def scratch(self) -> None:
        print(f"{self.name} scratches.")

class Canine(Animal):      # sibling
    def bark(self) -> None:
        print(f"{self.name} barks.")

class Avian(Animal):       # sibling
    def fly(self) -> None:
        print(f"{self.name} flies.")

# Wide tradeoffs:
#   + Easy to reason about - every subclass is exactly one hop from Animal
#   + Changes to Animal only ripple one level down, low blast radius
#   - Siblings can't share behavior with each other without duplicating it
#     or pulling it back up into Animal (which then pollutes ALL siblings)

# ---------------------------------------------------------------------------
# Deep (Hierarchical) Inheritance - a chain of classes, each inheriting from
# the one before it. More than 1 level deep.
class LivingThing:
    def __init__(self, name: str) -> None:
        self.name = name

class Animal(LivingThing):             # level 1
    def eat(self) -> None:
        print(f"{self.name} is eating.")

class Feline(Animal):                  # level 2
    def scratch(self) -> None:
        print(f"{self.name} scratches.")

class Tiger(Feline):                   # level 3
    def roar(self) -> None:
        print(f"{self.name} roars.")

tiger = Tiger("Shere Khan")
tiger.eat()      # inherited from Animal (2 hops up)
tiger.scratch()  # inherited from Feline (1 hop up)
tiger.roar()     # defined on Tiger itself

# Deep tradeoffs:
#   + Maximum code reuse - each level only adds what's new to IT
#   + Models real "is-a-a-a" taxonomies well (Tiger IS-A Feline IS-A Animal)
#   - Fragile base class problem - a change anywhere up the chain can ripple
#     through every descendant, and the further down you are, the harder it
#     is to trace WHERE a method/attribute actually came from
#   - Deep chains tend to get brittle over time; favor composition over
#     inheritance once a chain gets past 2-3 levels

# Rule of thumb: reach for Wide first (flat, low-risk). Only go Deep when
# there's a genuine multi-level taxonomy and each level adds real behavior -
# not just because "it's technically an X".

# ---------------------------------------------------------------------------
# Why attribute type (public vs private) matters
# ---------------------------------------------------------------------------
# Refactoring:
# Since the attribute is public, it's directly accessible from anywhere - no
# method required, no boundary enforced. That accessibility means any part
# of the codebase can reach in and read it directly, without you ever
# knowing it happened. So when refactor time comes, you have no reliable
# way to know how many places touched that attribute directly versus went
# through a method - the accessibility that made it convenient earlier is
# the same thing that makes it untraceable now.
#
# Since it's private, direct access from outside the class is blocked by
# design - only the class's own methods can reach it. That means every
# consumer, from day one, was forced through a method you control. So when
# you refactor the internal representation, you have control over the
# blast radius: you only need to update the logic inside that method,
# because there was never a second path in.
#
# Even across inheritance, this holds: since the attribute is
# name-mangled, a subclass can't reach it directly either - it still has
# to go through the parent's getter, same as any outside caller. Privacy
# isn't weakened by inheritance; it's still fully contained to the class
# that defined it.
#
# Mutation:
# Since the attribute is public, it can be bypassed - any code, anywhere,
# can assign to it directly without going through your mutation method.
# That means every guardrail and validation check you wrote inside that
# method is optional, not enforced. The moment someone writes to the
# attribute directly, the object can land in an invalid state
# immediately, with no error and no warning, because the attribute itself
# carries no memory of your rules.
#
# Since it's private, that bypass path doesn't exist - the only way to
# change the value is through the method you wrote, which means your
# validation is guaranteed to run every time, for every caller, with no
# exceptions. You have control not just over HOW the attribute mutates,
# but over the certainty that nothing else in the codebase - including
# code written by other developers who never saw your validation logic -
# can touch it any other way.


# ---------------------------------------------------------------------------
# Polymorphism - " Poly" means many "Morph" means to transform
# Polymorphism in programming is the ability to present the same interface (function or method signatures) for many different underlying forms (data types).

# Case study: Dragon.in_area overriding Unit.in_area (polymorphism.py)
#
# - Unit.in_area treats the unit as a single POINT: is (pos_x, pos_y) inside
#   the given box?
# - Dragon.in_area overrides this with a different definition for a
#   different kind of object: does the dragon's own hit box OVERLAP the
#   given box? Same method name, same signature, different behavior per
#   class - that's polymorphism.
# - The target area is never stored on the instance. x1, y1, x2, y2 arrive
#   fresh on every call and are wrapped in a throwaway Rectangle just for
#   that check - the object has no memory of "the area", only of itself.
#
# Mechanics of self.__hit_box.overlaps(hit_box):
# - Whichever object sits LEFT of the dot is mechanically bound to self
#   inside the method. This is a fixed rule of Python method calls, not a
#   style choice.
# - The argument in the parentheses fills the other parameter (rect).
# - Since both self.__hit_box and hit_box are Rectangle instances, either
#   one could technically call .overlaps() on the other, and since overlaps
#   is symmetric (A overlaps B implies B overlaps A), the boolean result
#   would be identical either way.
#
# Mechanical correctness vs semantic correctness:
# - Both self.__hit_box.overlaps(hit_box) and hit_box.overlaps(self.__hit_box)
#   pass here - the math doesn't care which side is "self".
# - But the code should still read as "the dragon checks itself against the
#   area" (self.__hit_box.overlaps(hit_box)), because that matches the real
#   -world direction of the question (dragon attacks area, not the
#   reverse). Writing it backwards would still pass tests but would
#   misrepresent intent to the next reader.
# - Lesson: passing tests only proves mechanical correctness. Matching the
#   real-world relationship the code models is a separate, equally
#   important concern - optimize for both.
#
# Reuse potential: the constructor also stores fire_range, unused in this
# lesson. The same Rectangle/overlaps pattern used for __hit_box could
# later back a can_attack_area(...) method built from fire_range instead -
# hit boxes, fire ranges, vision ranges, attack ranges could all reuse the
# same overlap-check logic instead of duplicating comparison code per
# feature. This is why encapsulating the check inside Rectangle.overlaps
# (rather than inlining it per-caller) was a good design choice.

# What polymorphism actually is, refined:
#
# - An instance is NOT "either" its parent type "or" its child type - it is
#   BOTH at once. A Dragon instance IS-A Unit (through inheritance) while
#   still fundamentally being a Dragon. Code that expects a plain Unit can
#   hold a Dragon and still get Dragon's own overridden methods - that dual
#   identity, resolved at runtime based on the object's real type, is the
#   mechanism that makes polymorphism work (dynamic dispatch).
#
# - Inheritance is the "first passage of transformation": the subclass
#   receives everything the parent has for free (attributes, methods) -
#   that's the shape being carried forward before any overriding happens.
#
# - Method overriding = a subclass providing the same method name/signature
#   as its parent, but a different implementation. Which version runs is
#   chosen automatically based on the object's actual type at runtime, not
#   by the variable's declared type.
#       - The relevance of method overriding shows up the moment you have a 
#         collection of mixed types and want to treat them uniformly.
#       - Imagine a list similar to your: (dragons.py/polymorphism.py)
units: list[Unit] = [Archer(40, 10), Elf(40, 10, 9), Dragon("Green", 0, 0, 4, 4, 3)]
for u in units:
    if u.in_area(0, 0, 10, 10):
        print(f"{u.name} is in the area")

# Without polymorphism, that loop wouldn't be possible — you'd need something like:
for u in units:
    if isinstance(u, Dragon):
        # do the rectangle-overlap check
    elif isinstance(u, Elf):
        # do the point check, but also stealth logic?
    elif isinstance(u, Archer):
        # do the point check
#   - Every time you add a new unit type, you'd have to go back and add another 
#     branch to every place in the codebase that loops over units.
# 
# - Having Method Signatures and Method Overriding provides:   
#   1. One call site, many behaviors — same line of code works correctly 
#               for every subclass, present or future.
#   2. Extensibility without touching existing code — add a Griffin subclass 
#               tomorrow with its own in_area override, and this loop keeps 
#               working with zero edits (the Open/Closed Principle you already 
#               connected to earlier).
#    3. Decoupling — the code that uses units doesn't need to import or know about 
#               every concrete subclass; it only needs to know the shape 
#               (signature) it can rely on.
#
# - Creating discardable/local instances of another class inside a method
#   (e.g. the temporary Rectangle built inside in_area) is NOT polymorphism
#   itself - it's a separate, related pair of concepts:
#     - composition: a class using instances of another class internally
#       to get its work done.
#     - encapsulation: the caller never sees those temporary objects -
#       they're purely an implementation detail hidden inside the method.
#
# - "All this can happen without refactoring the parent class" is the
#   Open/Closed Principle in action: Unit never had to change to support
#   Dragon's new overlap-based behavior. Classes should be open to
#   extension (via subclassing/overriding) but closed to modification
#   (the original class's code stays untouched).
#
# Operator Overloading:
# See Activities: ../activities/sword_operator_overloading.py
#                 ../activities/dragon_operator_overloading.py
#   - Since operands dont work inside custom classes like below
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2    # TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
#
#   - We can create a special method or "dunder methods" to enable operands
#       - for this example it would be __add__
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2 # p3 is (6, 8)

#---------------------------------------
# Operator Overload Functions
#---------------------------------------
# Operation             Operator    Method
# Addition               +          __add__
# Subtraction            -          __sub__
# Multiplication         *          __mul__
# Power                  **         __pow__
# Division               /          __truediv__
# Floor Division         //         __floordiv__
# Remainder (modulo)     %          __mod__
# Bitwise Left Shift     <<         __lshift__
# Bitwise Right Shift    >>         __rshift__
# Bitwise AND            &          __and__
# Bitwise OR             |          __or__
# Bitwise XOR            ^          __xor__
# Bitwise NOT            ~          __invert__
#---------------------------------------



