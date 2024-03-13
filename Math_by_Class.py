class Math:
    def pow(self, a, b):
        return a ** b

    def sqrt(self, a):
        return a ** (1 / 2)

    def sum(self, *args):
        result = 0
        for num in args:
            result += num
        return result

    def fabs(self, a):
        if a < 0:
            return -a
        else:
            return a

    def is_odd(self, a):
        return a % 2 != 0

    def is_even(self, a):
        return a % 2 == 0


print(Math().pow(2, 7))
print(Math().sqrt(9))
print(Math().sum(2, 3, 5, 6))
print(Math().fabs(-2.5))
print(Math().is_odd(5))
print(Math().is_even(5))
