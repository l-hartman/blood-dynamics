import random
import math


random.seed(111)

class Model(object):
    """
        x_n+1 - x_n = p(x_n) - d(x_n)o

        where:
            x_n is the blood cell count at time n;
            p is a function that represents the number of cells produced in one time unit;
            d is a function that measures the number of cells destroyed in one time unit;
    """


    def __init__(self):
        # destruction coefficient, # between 0 and 1
        self.a = random.uniform(0, 1)
        self.b = 2
        self.r = 3
        self.s = 4
        self.a_bar = (self.a, self.b, self.r, self.s)

    def p(self, x_n):
        """Lasota (1977) production function"""
        return self.b * x_n ** self.r * math.e ** (-self.s * x_n)

    def d(self, x_n):
        """for each timestep a constant fraction of cells are destroyed"""
        return self.a * x_n

    def f(self, x):
        return (1 - self.a) * x + self.p(x)


def main():
    pass


if __name__ == "__main__":
    main()
