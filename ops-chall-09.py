#!/usr/bin/env python3
#
# Script Name:  ops-challenge-09
# Author:  Ben_Podawiltz
# Date of last revision:  5.14.21

#################################

# Purpose: Create a Python script that includes the following:
# [*] 1. Assign to a variable a list of ten string elements.
# [*] 2. Print the fourth element of the list.
# [*] 3. Print the sixth through tenth element of the list.
# [*] 4. Change the value of the seventh element to “onion”.
#
#################################
# Import libraries

#################################

# Global variables

fellow_ship = ["Frodo", "Samwise", "Merry", "Pippin", "Aragon",
               "Boromir", "Legolas", "Gimili", "Gandalf", "Gollum"]  # list items are ordered, changeable, and allow duplicate values

#################################

# list/index

# output for index item 4 in list: index starts at 0,1,2...
print("This is the 4 item in the list:")
print(fellow_ship[3])

# output for index items in a range: prints items 6 - 10
print("This is the items range 6 - 10:")
print(fellow_ship[5:10])
# changes value in defined position in index to new value in "str"
print("This is the 7th item in list changed to 'onion':")
fellow_ship[6] = "onion"

print(fellow_ship)

#################################

# append

fellow_ship.append("Galadriel")  # adds/appends "str" to list
print("This is the list with the appended item:")
print(fellow_ship)

#################################

# count

x = fellow_ship.count("Samwise")
print("This is the count of the 'string' Samwise:")
print(x)

#################################

# copy
print("This is the copy of the list:")
O = fellow_ship.copy()
print(O)


#################################
ring = (1, 2, 4, .99,)
# extend method adds the specified list elements (or any iterable) to the end of the current list
fellow_ship.extend(ring)
print("This is the list with extended tuple:")
print(fellow_ship)

##################################

# index method returns the position at the first occurrence of the specified value
Gondor = fellow_ship.index("Boromir")
print("This is the index number for Boromir:")
print(Gondor)

##################################

# insert method inserts the specified value at  the specified position
fellow_ship.insert(6, "Thorin Oakenshield")
print("This is the insert of value 'str' at index postion 6:")
print(fellow_ship)

##################################

# pop removes the element at the specified position
Dwarf = fellow_ship.pop(6)
print("This is the element being removed:")
print(Dwarf)

###################################

# remove method removes the first occurence of the element with  the specified value
fellow_ship.remove("Galadriel")
print("This the list with Galadriel removed:")
print(fellow_ship)

###################################

# reverse method reverses the order of list [no parameters to pass]
fellow_ship.reverse()
print("This is the list reversed:")
print(fellow_ship)

###################################

# sort method sorts the list ascending by default


def myFunc(e):
    return e['rings']


species = [
    # list of dictionaries based on the "rings" value of the dictionaries
    {'species': 'Elf', 'rings': 3},
    {'species': 'Dwarfs', 'rings': 7},
    {'species': 'Men', 'rings': 9}
]

species.sort(key=myFunc)
print("This is the list of 'rings' each species has:")
print(species)

####################################

# clear
fellow_ship.clear()
print("This is the list cleared:")
print(fellow_ship)

#################################


# Source:[https://www.w3schools.com/python/ref_list_index.asp]


# End
