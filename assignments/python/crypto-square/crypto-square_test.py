from crypto import Crypto, chunks
import unittest

class CryptoTest(unittest.TestCase):
    def test_normalize_strange_characters(self):
      crypto = Crypto('s#$%^&plunk')
      self.assertEqual("splunk", crypto.normalize_plaintext())

    def test_normalize_with_numbers(self):
      crypto = Crypto('1, 2, 3 GO!')
      self.assertEqual("123go", crypto.normalize_plaintext())

    def test_size_of_small_square(self):
      crypto = Crypto('1234')
      self.assertEqual(2, crypto.size())

    def test_size_of_slightly_larger_square(self):
      crypto = Crypto('123456789')
      self.assertEqual(3, crypto.size())

    def test_size_of_non_perfect_square(self):
      crypto = Crypto('123456789abc')
      self.assertEqual(4, crypto.size())

    def test_plaintext_segments(self):
      crypto = Crypto('Never vex thine heart with idle woes')
      self.assertEqual(
          ["neverv", "exthin", "eheart", "withid", "lewoes"],
          list(crypto.plaintext_segments())
      )

    def test_other_plaintext_segments(self):
      crypto = Crypto('ZOMG! ZOMBIES!!!')
      self.assertEqual(
          ["zomg", "zomb", "ies"],
          list(crypto.plaintext_segments())
      )

    def test_ciphertext(self):
      crypto = Crypto('Time is an illusion. Lunchtime doubly so.')
      self.assertEqual(
          "tasneyinicdsmiohooelntuillibsuuml",
          crypto.ciphertext()
      )

    def test_another_ciphertext(self):
      crypto = Crypto('We all know interspecies romance is weird.')
      self.assertEqual(
          "wneiaweoreneawssciliprerlneoidktcms",
          crypto.ciphertext()
      )

    def test_normalized_ciphertext(self):
      crypto = Crypto('Madness, and then illumination.')
      self.assertEqual(
          'msemo aanin dninn dlaet ltshu i',
          crypto.normalize_ciphertext()
      )

    def test_more_normalized_ciphertext(self):
      crypto = Crypto('Vampires are people too!')
      self.assertEqual(
          'vrela epems etpao oirpo',
          crypto.normalize_ciphertext()
      )

if __name__ == '__main__':
    unittest.main()
