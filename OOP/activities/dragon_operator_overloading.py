class Dragon:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f"I am {self.name}, the {self.color} dragon"

