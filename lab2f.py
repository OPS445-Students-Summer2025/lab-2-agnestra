#!/usr/bin/env python3

#Author: Agnestra Mahat
#Author ID: 12893938
#Date Created: 2025/06/05

import sys

arguments = sys.argv

# This  assigns the value of int(sys.argv[1]) to an object named timer 
timer = int(sys.argv[1])

# While loop that repeats itself until the bomb blasts
while timer > 0:
    print(timer)
    timer = timer - 1


# kaboom
print("blast off!")



