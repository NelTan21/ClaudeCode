class Human:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name
        # Best to practice that defined attributes have their own call method in their class
        # get_name can be used to call the names of the inheritors(Archer and Crossbownman)
        # Since they have no way of directly accessing self.__name in their own class

## don't touch above this line


class Archer(Human):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self) -> int:
        return self.__num_arrows
        # Best to practice that defined attributes have their own call method in their class
        # get_num_arrows can be used to check the arrow count of the inheritor(Crossbownman)
        # Since it has no way of directly accessing self.__num_arrows in their own class

    def use_arrows(self, num: int) -> None:
        if self.__num_arrows < num:
            raise Exception("not enough arrows")
        self.__num_arrows -= num
        # Best to practice that defined attributes have their own call method in their class
        # use_arrows can be used to subtract the arrow count of the inheritor(Crossbownman)
        # Since it has no way of directly subtracting self.__num_arrows in their own class

class Crossbowman(Archer):
    def __init__(self, name: str, num_arrows: int) -> None:
        super().__init__(name, num_arrows)

    def triple_shot(self, target: Human) -> str:
        self.use_arrows(3) 
        # cant directly subtract from an attribute of the parent class
        # Class Archer / Method use_arrows was the gateway to subtract arrows
        return f"{target.get_name()} was shot by 3 crossbow bolts"
        # cant directly check for the name if the crossbowman self.__name in their own class
        # Class Human / Method get_names was the gateway to check the name of the crossbowman
