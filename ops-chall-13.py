#!/usr/bin/env python3
#
# Script Name:  ops-challenge-13
# Author:  Ben_Podawiltz
# Date of last revision:  5.26.21

#################################

# Purpose:
# Prompt the user to type a string input as the variable for your destination URL.
# Prompt the user to select a HTTP Method of the following options:
# [+] 1. GET
# [+] 2. POST
# [+] 3. PUT
# [+] 4. DELETE
# [+] 5. HEAD
# [+] 6. PATCH
# [+] 7. OPTIONS
# [] 8. Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# [] 9. Using the requests library, perform a GET request against your lab web server.
# [+] 10.For the given header, translate the codes into plain terms that print to the screen; for example, a ‘404’ error should print ‘Site not found’ to the terminal instead of ‘404’.
# [+] 11. For the given URL, print response header information to the screen.
#

##################################

# Import OS modules/libraries
import requests
import requests.api

##################################

# Global Variables

url = input(
    "\nPlease enter destination URL in this format [https://webserver.com]:\n")


#################################
# Menu for choosing HTTP method
print("\nPlease select an HTTP Method from the following menu:\n")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. HEAD")
print("6. PATCH")
print("7. OPTIONS")
method = input()
# user input required for method selection
#################################

if method == '1':
    # GET or retrieve data from a specified resource

    # object for storing results of the request - GET
    getresponse = requests.get(url)
    if getresponse.status_code == 200:
        print("Success!")
    elif getresponse.status_code == 404:
        print("Site Not Found")
    else:
        print('Other codes found')
    print(getresponse.headers)

###################################

elif method == '2':

 # object for storing results of the request - POST
    postresponse = requests.post(url)
    if postresponse.status_code == 200:
        print("\nSuccess!")
    elif postresponse.status_code == 404:
        print("\nSite Not Found")
    else:
        print("\nOther codes found")
    print(postresponse.headers)

#####################################

elif method == '3':

    # object for storing results of the request - PUT
    put_r = requests.put(url)
    if put_r.status_code == 200:
        print("Success!")
    elif put_r.status_code == 404:
        print("Site Not Found")
    else:
        print("Other codes found")
    print(put_r.headers)

######################################

elif method == '4':

    # object for storing results of the request - DELETE
    del_r = requests.delete(url)
    if del_r.status_code == 200:
        print("Success!")
    elif del_r.status_code == 404:
        print("Site Not Found")
    else:
        print("Other codes found")
    print(del_r.headers)

######################################

elif method == '5':
    # object for storing results of the request - DELETE
    head_r = requests.head(url)
    if head_r.status_code == 200:
        print("Success!")
    elif head_r.status_code == 404:
        print("Site Not Found")
    else:
        print("Other codes found")
    print(head_r.headers)

#########################################

elif method == '6':

    # object for storing results of the request - HEAD
    patch_r = requests.head(url)
    if patch_r.status_code == 200:
        print("Success!")
    elif patch_r.status_code == 404:
        print("Site Not Found")
    else:
        print("Other codes found")
    print(patch_r.headers)

#######################################

elif method == '7':
    # object for storing results of the request - OPTIONS
    opt_r = requests.options(url)
    if opt_r.status_code == 200:
        print("Success!")
    elif opt_r.status_code == 404:
        print("Site Not Found")
    else:
        print("Other codes found")
    print(opt_r.headers)

else:
    print("Error: Invalid Entry")

#########################################

# Comment: Could add a while loop to keep script alive. Initially tried a 3rd nested function to seperate the iteration in each method choice. Each method choice would then call a corresponding single function versus the code present in each block. Futher development.

# Sources: https://realpython.com/python-requests/
