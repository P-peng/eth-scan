#！/usr/bin/python3
import random

import main
from config.EthConfig import EthConfig


def t1():
    x = 1
    for x in range(x, 10):
        print(random.randint(0,15))

    print(len("b8d44e45b37d44a2e44d29d66cb4ea886fc78961f0ca79be89b297cb781e7396"))

    print("k " + "b")

if __name__ == "__main__":
    # main.get_random()

    for x in range(len(EthConfig.keys)):
        print(EthConfig.get_key())

    print("1" + "1")
