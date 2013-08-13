from atbash import encode
import unittest

class est(unittest.TestCase):
    def test_encode_no(self):
        self.assertEqual('ml', encode('no'))

    def test_encode_yes(self):
        self.assertEqual('bvh', encode('yes'))

    def test_encode_OMG(self):
        self.assertEqual('lnt', encode('OMG'))

    def test_encode_O_M_G(self):
        self.assertEqual('lnt', encode('O M G'))

    def test_encode_long_word(self):
        self.assertEqual('nrmwy oldrm tob', encode('mindblowingly'))

    def test_encode_numbers(self):
        self.assertEqual(
            'gvhgr mt123 gvhgr mt',
            encode('Testing, 1 2 3, testing.')
        )

    def test_encode_sentence(self):
        self.assertEqual(
            'gifgs rhurx grlm',
            encode('Truth is fiction.')
        )

    def test_encode_all_the_things(self):
        plaintext = 'The quick brown fox jumps over the lazy dog.'
        cipher = 'gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt'
        self.assertEqual(cipher, encode(plaintext))

if __name__ == '__main__':
    unittest.main()
