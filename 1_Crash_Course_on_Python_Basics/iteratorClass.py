class PowerTwo:
    """
    This class is an iterator of the powers of two.
    """

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = PowerTwo(5)
i = iter(a)
while True:
    try:
        print(next(i))
    except StopIteration:
        break