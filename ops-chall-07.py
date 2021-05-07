#!/usr/bin/env python3
#
# Script Name:  ops-challenge-07
# Author:  Ben_Podawiltz
# Date of last revision:  5.6.21

#################################

# Purpose: Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.

# Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

#################################
# Import libraries

import os

# Declaration of variables
# Read user input here into a variable
user_input = input("Please Enter an Filepath from Root [/]:")


print("Filepath from Root is: " + user_input)
print('*' * 25)

# Declaration of functions
# Declare a function here

for (root, dirs, files) in os.walk(user_input, topdown=False):
    # Add a print command here to print ==root==
    print(root)
    for name in dirs:
        print(os.path.join(root, name))
    for name in files:
        print(os.path.join(root, name))
    ### Break Line ###
    print('*' * 25)
    print("***********END***********")

# Main


# Comment: This works for /var /tmp etc and other directories but not directories I created (?) For instance I cannot open my github dir. I suppose this is because this is for directories only originating from [/] root and not $HOME  or /home/username. How can I adjust this script to work on any directory within the FHS

############################################

# Sources: https://www.geeksforgeeks.org/os-walk-python/ https://www.tutorialspoint.com/python3/os_walk.htm
#
# End
