import random

Card = tuple[str, str]


class DeckOfCards:
    SUITS: list[str] = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS: list[str] = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self) -> None:
        self.__cards: list[Card] = []
        self.create_deck()

    def create_deck(self) -> None:
        for suit in DeckOfCards.SUITS:
            tuple1 = suit
            #print(f"This is the SUIT({tuple1})")
            for rank in DeckOfCards.RANKS:
                tuple2 = rank
                #print(f"This is the RANK({tuple2})")
                self.__cards.append((tuple2, tuple1))
            #print(f"This is the tuple list for({tuple1}), {self.__cards}")
        #print(f"This is the complete combination list, {self.__cards}")
                

    def shuffle_deck(self) -> None:
        random.shuffle(self.__cards)

    def deal_card(self) -> Card | None:
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop()

    # don't touch below this line

    def __str__(self) -> str:
        return f"The deck has {len(self.__cards)} cards"

