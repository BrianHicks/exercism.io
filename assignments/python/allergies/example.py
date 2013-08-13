class Allergies(object):
    ALLERGENS = [
        "eggs", "peanuts", "shellfish", "strawberries",
        "tomatoes", "chocolate", "pollen", "cats"
    ]

    def __init__(self, score):
        self.score = score

    def __iter__(self):
        for allergen in self.ALLERGENS:
            if self.is_allergic_to(allergen):
                yield allergen

    def is_allergic_to(self, item):
        """
        This project uses a concept called bitflagging where each new allergen
        is a power of 2. If you want to see how this works, try using `bin` to
        turn `self.score` into a binary string. The result is "100010" when the
        score is 34. The first 1 is chocolate, the second 1 is peanuts. 32 + 2
        == 34.

        This works because even if all the allergens below 'cats' were active,
        their total value would be 127.
        """
        index = self.ALLERGENS.index(item)
        return self.score & (2 ** index) > 0
