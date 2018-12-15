#
# ==========================
# > SOFY - Core ---------------
# > By S@n1x D4rk3r --------------
# ==================================
#

# Imports dependencies
import sys
import os

# -------------------------------------------------------------------------------------------
# Global Variables
# -------------------------------------------------------------------------------------------
get_parameter = ""
current_os = ""
current_python = sys.version_info[0]

# -------------------------------------------------------------------------------------------
# Methods
# -------------------------------------------------------------------------------------------
#
# Redefine print for python version
#
def printIt(message):
    if current_python == 2:
        print message
    elif current_python == 3:
        print (message)
    else :
        os.system("Your Current Python version looks to be not recognize")
        presentation()

#
# Redifine the getting value for python version
#
def inputIt(message):
    if current_python == 2:
        return raw_input("SF > "+message)
    elif current_python == 3:
        return input("SF > "+message)
    else :
        os.system("Your Current Python version looks to be not recognize")
        presentation()

#
# Just for a specific print log
#
def sofyPRINT(message):
    printIt ("SF > "+message)

#
# The presentation && Cleaning method
#
def presentation():
    # Cleaning the console
    os.system("cls")
    printIt ("\n----------------------------------------------------------")
    printIt ("---------------------- S   O   F   Y ---------------------")
    printIt ("----------------------------------------------------------")
    printIt ("__________________________________By S@n1x-D4rk3r_________\n")
    sofyPRINT("Welcome to SoFy, a software manager made for humans!")
    ## Checking the current OS
    sofyPRINT("OS detected: '"+current_os+"'")
    sofyPRINT("Python version detected: '"+str(current_python)+"'")

#
# Check the current OS
#
def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        current_os = sys.platform
        return sys.platform
    current_os = platforms[sys.platform]
    return platforms[sys.platform]

def help_func():
    sofyPRINT("SoFy help you fast installing your software, list of commands:")
    printIt("\nh or help: to get Helping functions \nEx: help")
    printIt("\nq or quit: to exit SoFy \nEx: quit")
    printIt("\ng or get : write this command and hit Enter first, and next in 'Name(s):' just write software you want.")
    printIt("Ex: Name: VLC,Google Chrome\n")

def quit_func():
    sofyPRINT("Thank you for using SoFy");
    sys.exit()

def get_func():
    sofyPRINT("What do you want me to get for you on the WEB?")
    to_find = inputIt("Name(s):")

def Switch(value):
    if value.lower() == "h" or value.lower() == "help":
        help_func()
    if value.lower() == "q" or value.lower() == "quit":
        quit_func()
    if value.lower() == "e" or value.lower() == "exit":
        quit_func()
    if value.lower() == "g" or value.lower() == "get":
        get_func()
    else:
        sofyPRINT("Command not found, please try again!")
        main()

# Get Param and act
def main():
    # Get the current parameter
    get_parameter = inputIt("Command (help / h or quit / q to stop): ")
    # switch case on the parameter given
    Switch(get_parameter)

# -------------------------------------------------------------------------------------------
# Main source code
# -------------------------------------------------------------------------------------------
current_os = get_platform()

# Presentation method
presentation()

## Start SoFy Core
main()

## Pause the batch script
os.system("pause")