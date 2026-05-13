import sys
import os

# Adds the directory of the current script to the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import math_utils  # Now this should work


import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print("Time:", end - start)

    return wrapper



@timer
def test():

    for i in range(1000000):
        pass

test()



@timer
def test():

    for i in range(1000000):
        pass

test()

import math_utils

print(math_utils.add(2, 3))