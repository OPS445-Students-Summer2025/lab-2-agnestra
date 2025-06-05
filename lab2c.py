#!/usr/bin/env python3

import sys

arguments = sys.argv

#The line displays the screen name
scriptname  = sys.argv[0] 

#This line dusplays the 1st argument as the name
Name = sys.argv[1]

#This line dislays the 2nd argument as the age 
Age = sys.argv[2]

#This is why I was getting an assertion error, this should not have been a part of the output mistook it.
#print (scriptname+' '+Name +' '+str(Age))

#This line gives you the required output
print('Hi '+Name+', you are '+str(Age)+' years old.')




#This line prompts the user for name
#Name = sys .argv[1] 

#This line prompts the user fo their age
#Age = age = sys.argv[2]

#This line prints Hi Name, you are Age years old.
#print('Hi ' + Name + ', you are ' + str(Age) + ' years old.')

# The input value also prints the name and age value so the print statements for name and age were not needed.
#This line prints the name 
#print('Name: ' + Name)

#This line prints the age
#print('Age: ' + Age)