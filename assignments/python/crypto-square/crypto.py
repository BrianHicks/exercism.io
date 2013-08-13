from itertools import izip_longest
from math import sqrt, ceil
import re

def chunks(iterable, size):
    for n in range(0, len(iterable), size):
        yield iterable[n:n+size]


class Crypto(object):
    def __init__(self, plaintext):
        self.plaintext = plaintext

    def normalize_plaintext(self):
        return re.sub('\W', '', self.plaintext.lower())

    def size(self):
        return int(ceil(sqrt(len(self.normalize_plaintext()))))

    def plaintext_segments(self):
        return chunks(self.normalize_plaintext(), self.size())

    def ciphertext(self):
        return ''.join(
            ''.join(segment) for segment
            in izip_longest(*self.plaintext_segments(), fillvalue='')
        )

    def normalize_ciphertext(self):
        return ' '.join(chunks(self.ciphertext(), 5))
