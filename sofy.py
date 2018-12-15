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
        return raw_input(message)
    elif current_python == 3:
        return input(message)
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
# Encrypt/Decrypt Key From SOFY
# Usage:
# secret_data = "239054"
# print sf_crypt_string(secret_data, encode=True)
# print sf_crypt_string(sf_crypt_string(secret_data, encode=True), decode=True)
#
def sf_crypt_string(data, key='S@n1x-D4rk3r', encode=False, decode=False):
    from itertools import izip, cycle
    import base64
    if decode:
        data = base64.decodestring(data)
    sfed = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(sfed).strip()
    return sfed
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
    sofyPRINT("SoFy help you fast installing your software, list of commands:");

def quit_func():
    sofyPRINT("Thank you for using SoFy");
    sys.exit()

def Switch(value):
    if value.lower() == "h" or value.lower() == "help":
        help_func()
    if value.lower() == "q" or value.lower() == "quit":
        quit_func()
    if value.lower() == "e" or value.lower() == "exit":
        quit_func()
    else:
        sofyPRINT("Command not found, please try again!")
        main()

# Get Param and act
def main():
    # Get the current parameter
    get_parameter = inputIt("SF > Command (help / h or quit / q to stop): ")
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