class Trinary(object):
    BASE = 3

    def __init__(self, decimal):
        self.digits = [
            digit for digit
            in reversed(decimal)
            if digit in '012'
        ]

    def __int__(self):
        return sum(
            int(digit) * self.BASE ** index for index, digit
            in enumerate(self.digits)
        )
