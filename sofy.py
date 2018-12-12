#################
# SOFY Core
# By Sanix Darker
#################

# Imports
import platform
import sys
import os

# Methods
def sofyPRINT(message):
    print "SF > "+message

def presentation():
    os.system("cls")
    print "\n----------------------------------------------------------"
    print "---------------------- S   O   F   Y ---------------------"
    print "----------------------------------------------------------"
    print "__________________________________By S@n1x-D4rk3r_________\n"
    sofyPRINT("Welcome to SoFy, a software manager made for humans!")

presentation()
## Checking the current OS
if platform.system() == 'Windows':
    sofyPRINT("OS detected: '"+platform.platform()+"'")
elif platform.system() == 'Linux':
    sofyPRINT("OS detected: "+platform.platform())
elif platform.system() == 'Mac':
    sofyPRINT("OS detected: "+platform.platform())
else:
    sofyPRINT("SoFy is not yet configured for this kind of OS")

os.system("pause")