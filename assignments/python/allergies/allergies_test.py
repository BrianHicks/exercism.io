from allergies import Allergies
import unittest

class AllergiesTest(unittest.TestCase):
    def test_no_allergies_at_all(self):
        allergies = Allergies(0)
        self.assertEqual([], list(allergies))

    def test_allergic_to_just_eggs(self):
        allergies = Allergies(1)
        self.assertEqual(['eggs'], list(allergies))

    def test_allergic_to_just_peanuts(self):
        allergies = Allergies(2)
        self.assertEqual(['peanuts'], list(allergies))

    def test_allergic_to_just_strawberries(self):
        allergies = Allergies(8)
        self.assertEqual(['strawberries'], list(allergies))

    def test_allergic_to_eggs_and_peanuts(self):
        allergies = Allergies(3)
        self.assertEqual(['eggs', 'peanuts'], list(allergies))

    def test_allergic_to_more_than_eggs_but_not_peanuts(self):
        allergies = Allergies(5)
        self.assertEqual(['eggs', 'shellfish'], list(allergies))

    def test_allergic_to_lots_of_stuff(self):
        allergies = Allergies(248)
        self.assertEqual(
            ["strawberries", "tomatoes", "chocolate", "pollen", "cats"],
            list(allergies)
        )

    def test_allergic_to_everything(self):
        allergies = Allergies(255)
        self.assertEqual(
            [
                "eggs", "peanuts", "shellfish", "strawberries",
                "tomatoes", "chocolate", "pollen", "cats"
            ],
            list(allergies)
        )

    def test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_is_allergic_to_eggs(self):
        allergies = Allergies(1)
        self.assertTrue(allergies.is_allergic_to('eggs'))

    def test_allergic_to_eggs_in_addition_to_other_stuff(self):
        allergies = Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))

    def test_ignore_non_allergen_score_parts(self):
        allergies = Allergies(509)
        self.assertEqual(
            [
                "eggs", "shellfish", "strawberries", 
                "tomatoes", "chocolate", "pollen", "cats"
            ],
            list(allergies)
        )

if __name__ == '__main__':
    unittest.main()
