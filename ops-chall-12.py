#!/usr/bin/env python3
#
# Script Name:  ops-challenge-12
# Author:  Ben_Podawiltz
# Date of last revision:  5.24.21

#################################

# Purpose:
# Create a Python script that fetches this information using Psutil:
# [+] 1. Time spent by normal processes executing in user mode
# [+] 2. Time spent by processes executing in kernel mode
# [+] 3. Time when system was idle
# [+] 4. Time spent by priority processes executing in user mode
# [+] 5. Time spent waiting for I/O to complete.
# [+] 6. Time spent for servicing hardware interrupts
# [+] 7. Time spent for servicing software interrupts
# [+] 8. Time spent by other operating systems running in a virtualized environment
# [+] 9. Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
# Stretch Goals
# [+] 10. Save the information to a .txt file.
# [] 11. Email the .txt file to yourself using Sendmail.

#

##################################

# Import OS modules/libraries
import psutil

##################################

# Global Variables


#################################
# using with statement for exception handling; open a text file and close the file at the end of the block
with open("output.txt", "a") as f:
    print("user = time spent by normal processes executing in user mode; nice = time spent by priority processes executing in user mode; system =  time spent by processes executing in kernel mode; idle = time when system was idle; iowait = time spent waiting for I/O to complete; irq = time spent for servicing hardware interrupts; softirq = time spent for servicing software interrupts; guest = time spent rrunning a virtual CPU for guest operating system under the control of the Linux kernel", file=f)
    print("*************************************************************", file=f)
    print(psutil.cpu_times(), file=f)
    print("*************************************************************", file=f)
    print("Number of cores in system:", psutil.cpu_count(), file=f)
    print("\nNumber of physical cores in system:", file=f)
    print("*************************************************************", file=f)
    print("\nVirtual memory:", psutil.virtual_memory(), file=f)
    print("*************************************************************", file=f)
    print("\nDetails of disk partitions:", psutil.disk_partitions(), file=f)
    print("*************************************************************", file=f)
    print("\nDisk usage statistics:", psutil.disk_usage('/'), file=f)
    print("*************************************************************", file=f)
    print("\nUsers connected on the system:", psutil.users(), file=f)

##################################################

# Comment: Adding the with block output all data to the textfile but did not print to the screen. The challege first called for print to screen, which executed well until the with block output data to the textfile.


# Sources https://www.geeksforgeeks.org/with-statement-in-python/ https://www.geeksforgeeks.org/psutil-module-in-python/

# End
