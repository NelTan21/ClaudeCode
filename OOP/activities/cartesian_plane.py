class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

# 1. Nested loop + tuple comparison (your first correct version — brute-forces every point in the box):
def in_area_1(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
    for x in range(x_1, x_2 + 1):
        for y in range(y_1, y_2 + 1):
            if (self.pos_x, self.pos_y) == (x, y):
                return True
    return False

# 2. range membership (what you have now — O(1) per axis, no loop):
def in_area_2(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
    return self.pos_x in range(x_1, x_2 + 1) and self.pos_y in range(y_1, y_2 + 1)

#3. Direct comparison operators (the reference solution style — no fencepost +1 needed):
def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
    return (
        self.pos_x >= x_1
        and self.pos_x <= x_2
        and self.pos_y >= y_1
        and self.pos_y <= y_2
    )

class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int) -> None:
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

        print(f"This is the fire range: {self.__fire_range}")

    def breathe_fire(self, x: int, y: int, units: list[Unit]) -> list[Unit]:
        units_hit = []
            return (
        self.pos_x >= x_1
        and self.pos_x <= x_2
        and self.pos_y >= y_1
        and self.pos_y <= y_2
    )print(f"This is the center{x,y}")
        print(f"this is the range({self.__fire_range})")
        print((x-self.__fire_range), (y-self.__fire_range), (x+self.__fire_range), (y+self.__fire_range))
        for unit in units:
            print(f"Unit({unit.name}) is in ({(unit.pos_x, unit.pos_y)})")
            print(f"Checking if unit({unit.name}) is in the area...")
            if unit.in_area((x-self.__fire_range), (y-self.__fire_range), (x+self.__fire_range), (y+self.__fire_range)) == True:
                print(f"Unit ({unit.name}) was hit...")
                units_hit.append(unit)
                continue
            print(f"Unit ({unit.name}) was not hit...")
        print(f"These are the units hit {units_hit}")
        return units_hit
