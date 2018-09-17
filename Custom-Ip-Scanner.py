# Caleb's Custom Network Scanner :3

# Importing needed sub Programs
# Socket Module allows connection to Servers and Clients
# Random Module allows us to randomise the art pictures on start-up
# OS Module allows Operating System Identification
# getnode module from uuid allows the identification of Hosts Mac Address
import socket
import random
import os
from uuid import getnode as get_mac
from datetime import datetime

# Retrives Host's IP Address
HOST = (socket.gethostbyname(socket.gethostname()))

# Retrieves Host's Mac Address and converts Mac to string format
HOST_MAC = get_mac()
HOST_MAC = str(HOST_MAC)

# Retrieves Host's Computer Name
HOST_NAME = (socket.gethostname())

# Art for when the program loads, Added for style
def ART_TA():
    print(" ")
    print("....__________..............................................................")
    print(".../__   ____/../^\.........../////////....////////....////////..///////////")
    print("....../ /......// \\\........//     //...//...........//............///......")
    print("...../ /......//...\\\....../////////...//......___...///////......///.......")
    print("..../ /......//.....\\\..../////........//_____///..//............///........")
    print(".../_/......//       \\\..//...///.......///////...////////......///.........")
    print("............................................................................")
    print("...../^\...........////////.....//....//..//////////.../////////..////////..")
    print("....// \\\.......//......//....//....//......///......//     //..//..........")
    print("...//---\\\.....//......//....//....//......///....../////////..////////.....")
    print("..//-----\\\...//......<<<...//....//......///....../////......//............")
    print(".//       \\\...////////.....//////....//////////..//...///...////////.......")

#art = ['art1','art2','art3']
#RAN_WA = random.choice(art)
#print(" ")
#print(RAN_WA)
ART_TA()

# Displays Host's IP, MAC and Computer Name
print(" ")
print(" Welcome to Caleb's Custom Network Scanner :3")
print(" ")
print(" Your IP Address is: " + '['+HOST+']')
print(" Your Mac Address is: " + '['+HOST_MAC+']')
print(" Your Computer Name is: " + '['+HOST_NAME+']')
print(" ")
print(" for more info type help ...")

def Hinput():
    print(" ")
    HOST_INPUT = input(' > ')
    if HOST_INPUT == 'help':
        HELP_COMMAND()
    elif HOST_INPUT == 'exit':
        EXIT_COMMAND()
    elif HOST_INPUT == 'scan':
        SCAN_COMMAND()
    elif HOST_INPUT == 'name':
        NAME_COMMAND()
    elif HOST_INPUT == 'host':
        HOST_COMMAND()
    elif HOST_INPUT == 'clear':
        CLEAR_COMMAND()
    elif HOST_INPUT == 'host ports':
        HOSTP_COMMAND()

def HELP_COMMAND():
    print(" ")
    print(" HOST INFO")
    print(" -  host : Displays your info Example; IP Address, Mac Address and Computer name")
    print(" -  host ports : Displays your open ports")
    print(" ")
    print(" SCAN COMMANDS")
    print(" - scan <targets ip> : Scans target ip for name and open ports")
    print(" - name <targets ip> : Scans tagets Computer Name")
    print(" ")
    print(" OTHER")
    print(" - exit : Exits program")
    print(" - clear : Clears screen of text")
    Hinput()

def EXIT_COMMAND():
    exit()

def SCAN_COMMAND():
    IP_INPUT = input(" Target's IP: ")
    TIME = datetime.now()
    TIME = str(TIME)
    print(" ")
    print(" Scan Started at " + "["+TIME+"]")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(1,500):
        sock.connect_ex((IP_INPUT,port))
        if port == True:
            port = str(port)
            print("port open on " + port)
    Hinput()

def NAME_COMMAND():
    IP_INPUT = input("Targets IP: ")
    TARGET_NAME = socket.getfqdn(IP_INPUT)
    print("Targets Name is " + "["+TARGET_NAME+"]")
    Hinput()

def HOST_COMMAND():
    print(" ")
    print(" Your IP Address is: " + '['+HOST+']')
    print(" Your Mac Address is: " + '['+HOST_MAC+']')
    print(" Your Computer Name is: " + '['+HOST_NAME+']')
    Hinput()

def HOSTP_COMMAND():
    pass

def CLEAR_COMMAND():
    pass

Hinput()
