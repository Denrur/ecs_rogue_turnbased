class Blocked:
    def __init__(self, value: bool):
        self.value = value

    def __add__(self, other):
        return Blocked(self.value or other.value)

    def __sub__(self, other):
        return Blocked(self.value != other.value)


if __name__ == '__main__':
    for i in [False, True]:
        for j in [False, True]:
            a = Blocked(i)
            b = Blocked(j)
            print(f'{i} + {j} = {(a + b).value}')
            print(f'{i} - {j} = {a - b}')
    print(Blocked(True).value)
