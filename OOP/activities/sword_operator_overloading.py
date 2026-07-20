class Sword:
    def __init__(self, sword_type: str) -> None:
        self.sword_type = sword_type

    def __add__(self, other: "Sword") -> "Sword":
        sword_types = ["bronze", "iron", "steel"]
        for type in range(len(sword_types)-1):
            if self.sword_type == sword_types[type]:
                if self.sword_type == other.sword_type:
                    return Sword(sword_types[type+1])
        raise Exception("cannot craft")
