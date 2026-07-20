class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int) -> None:
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )


# don't touch above this line
# ---------------------------------------------------------------------------
# 1. The target area is being provided a test location, where in the self has no stored memory of target area, so its dynamic based on provided inputs.
# 2. target area is conditioned to be true as a valid target if self(dragon) overlaps to it so in order to validate condition, the in area override method was created.
# 3. in_area override inputs 4 corners of the area's rectangle which is instantiated as a new instance.
# 4. since self.__hit_box and hit_box are now instances of the class Rectangle, they are now considered Rectangle objects.
# 5. Rectangle objects can call out Rectangle methods.
# 6. we used self.__hit_box as the getter of the method because it satisfies the self parameter of the method
# 7. hit_box was sent as an argument to satisfy the rect paramter.
# Note: 
# - The "left of the dot" before the "method" called would always be referred to as "self" and the one in the parenthesis would be the "parameter". 
# - My meaning of order for purpose is the thought that dragon is the one attacking an area and hit_box is the area being attacked, not the other way around. 
# - But in this specific activity, since what we are only finding if there is an overlap, 
# - The output would pass even if they were interchanged.

class Dragon(Unit):
    def __init__(
        self,
        name: str,
        pos_x: int,
        pos_y: int,
        height: int,
        width: int,
        fire_range: int,
    ) -> None:
        super().__init__(name, pos_x, pos_y)
        self.height = height
        self.width = width
        self.fire_range = fire_range
        self.__hit_box = Rectangle(pos_x -(width/2), pos_y - (height/2), pos_x + (width/2), pos_y + (height/2))
 This activity has these points:


    def in_area(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        hit_box = Rectangle(x1, y1, x2, y2)
        return self.__hit_box.overlaps(hit_box)
        
# ---------------------------------------------------------------------------
# don't touch below this line


class Rectangle:
    def overlaps(self, rect: "Rectangle") -> bool:
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self) -> float:
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self) -> float:
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self) -> float:
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self) -> float:
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
