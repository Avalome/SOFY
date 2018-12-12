#
#################
# SOFY Core
# By Sanix Darker
#################
#

# Imports
import platform
import sys
import os

# Methods
# Just for a specific print log
def sofyPRINT(message):
    print "SF > "+message

# The presentation/ Cleaning method
def presentation():
    os.system("cls")
    print "\n----------------------------------------------------------"
    print "---------------------- S   O   F   Y ---------------------"
    print "----------------------------------------------------------"
    print "__________________________________By S@n1x-D4rk3r_________\n"
    sofyPRINT("Welcome to SoFy, a software manager made for humans!")

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