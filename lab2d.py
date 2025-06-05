#!/usr/bin/env python3

import sys

arguments = sys.argv

#This line should print a usage message if zero arguments present, or if not exactly 2 arguments are provided when running the script 
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit()
    
#The line displays the name of the script
scriptname  = sys.argv[0] 

#This line displays the 1st argument as the name
Name = sys.argv[1]

#This line dislays the 2nd argument as the age 
Age = sys.argv[2]

#This line gives you the required output
print('Hi '+Name+', you are '+str(Age)+' years old.')

