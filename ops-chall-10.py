#!/usr/bin/env python3
#
# Script Name:  ops-challenge-10
# Author:  Ben_Podawiltz
# Date of last revision:  5.17.21

#################################

# Purpose: Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
# [+] 1. Equals: a == b
# [+] 2. Not Equals: a != b
# [+] 3. Less than: a < b
# [+] 4. Less than or equal to: a <= b
# [+] 5. Greater than: a > b
# [+] 6. Greater than or equal to: a >= b
# [+] 7. Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
# [+] 8. Create an if statement that includes both elif and else to execute when both if and elif are not met.
#
#################################
# Import libraries

#################################

# Global variables

# user_input = a
user_input = input("Please enter a numeric value for variable (a):")
# user_input1 = b
user_input1 = input("Please enter a numeric value for variable (b):")

#
#################################

# Functions


if user_input > user_input1:  # uses variable input to conditional if statement
    print("a is greater than b")
elif user_input < user_input1:  # if previous condition not true then do this
    print("b is greater than a")
else:  # all other condtions do this
    print("Two variables are equal")

    print("*******BREAK*********")
    print("\n")

if user_input >= user_input1:
    print("a is greater than or equal to b")
elif user_input <= user_input1:
    print("b is greater than or equal to a")

    print("******BREAK********")
    print("\n")

if user_input == user_input1:
    print("a is equal to b")
elif user_input != user_input1:
    print("a is not equal to b")

    print("******BREAK**********")
    print("\n")

# using AND to have two condtionals at outset of logic
if user_input > user_input1 and user_input >= user_input1:
    print("a is greater than/or equal to b")
# using OR as a logical operator to combine conditional statements
elif user_input < user_input1 or user_input != user_input1:
    print("a is less than b or not equal")

    print("****BREAK********")
    print("\n")

if user_input > user_input1:
    print("a is greater than b")
elif user_input >= user_input1:
    print("a is greater than or equal to b")
else:
    print("b is not equal to or is less than a")

####################################

# Source: https://www.w3schools.com/python/python_conditions.asp

# End
