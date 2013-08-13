import re
from string import maketrans, ascii_lowercase

ATBASH_TRANSLATION = maketrans(
    ascii_lowercase,
    ''.join(reversed(ascii_lowercase))
)

CHUNK_LENGTH = 5

def encode(plaintext):
    """encrypt a given string with the atbase method"""
    base = plaintext.lower().translate(ATBASH_TRANSLATION)
    alphanums = re.findall(r'\w', base)

    return ' '.join(
        ''.join(alphanums[n:n+CHUNK_LENGTH])
        for n in range(0, len(alphanums), CHUNK_LENGTH)
    )
