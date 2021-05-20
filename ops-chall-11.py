#!/usr/bin/env python3
#
# Script Name:  ops-challenge-11
# Author:  Ben_Podawiltz
# Date of last revision:  5.19.21

#################################

# Purpose: Using file handling commands ,
# [+] 1. create a Python script that creates a new .txt file
# [+] 2. appends three lines,
# [+] 3. prints to the screen the first line
# [+] 4. then deletes the .txt file
# Stretch Goal
# [] 5.Have your Python script open the CSV or JSON of your Azure AD Audit Log and return customized information from it, such as a filtered view of most important information.

##################################

# Import OS modules
import os

##################################

# Global Variables

# create a new .txt file using "a" to appends to file
NT = open("eecummings.txt", "a")
new_txt_lines = ["pity this busy monter, manunkind", "not.Progress is a comfortable disease:",
                 "your victim [death and life safely beyond]"]  # variable that equals three lines of text
NTR = open("eecummings.txt", "r")
####################################

# Functions

# writes variable for lines into variable for open and write text
NT.writelines(new_txt_lines)
NT.close()  # closes text file


print(NTR.readline())  # reads the first line of the textfile
NTR.close()

# if/else to determine text file existance, if so - delete; else: print
if os.path.exists("eecummings.txt"):
    os.remove("eecummings.txt")
else:
    print("The file does not exist")

########################################

# Comment: readlines read all three of the appended strings of text. It did not distinguish the first string of text as the first line of the text file. When used in a preexisting document it will read the first line only.


# Sources: https://www.pythonforbeginners.com/files/python-file-handling

#

# End
