class Card():
    # Class attributes defining the valid options for a card
    RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITES = ["HEART", "DIAMOND", "SPADE", "CLUBS"]

    def __init__(self, suite, rank):
        # Type checking: Ensure the inputs are strings
        if not isinstance(suite, str):
            raise TypeError(f"Suite expected to be a string got {type(suite).__name__}")
        
        if not isinstance(rank, str):
            # Fixed a typo from the image (was 'Suite expected' here too)
            raise TypeError(f"Rank expected to be a string got {type(rank).__name__}")

        # Convert to uppercase to make the validation case-insensitive
        suiteUpper = suite.upper()
        rankUpper = rank.upper()

        # Validation: Check if the rank is in the approved list
        if rankUpper in Card.RANKS:
            pass
        else:
            # Fixed variable name to Card.RANKS to prevent a NameError
            raise TypeError(f"Added rank not in rank list {Card.RANKS}")

        # Validation: Check if the suite is in the approved list
        if suiteUpper in Card.SUITES:
            pass
        else:
            # Fixed variable name to Card.SUITES to prevent a NameError
            raise TypeError(f"Added suite not in suite list {Card.SUITES}")

        # Assign values to the instance attributes
        self.rank = rankUpper
        self.suite = suiteUpper

    def printCard(self):
        """Displays the card's rank and suite to the console"""
        print("Rank", self.rank)
        print("Suite", self.suite)

# Entry point for testing the class
if __name__ == "__main__":
    try:
        # This will fail and raise a TypeError because 'Joker' is not in SUITES
        card1 = Card(suite="Joker", rank="A")
        card1.printCard()
    except TypeError as e:
        print(f"Error: {e}")

    print("-" * 10)

    # This will succeed
    card2 = Card(suite="Clubs", rank="3")
    card2.printCard()