#!/usr/bin/python

from socket import *
# import socket
import optparse 
# optparse allows the use of flags
from threading import *
# A thread is a lightweight process. A process can do more than one unit of work concurrently by creating one or more threads
from termcolor import colored


def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort)) # develop a connection on parameters
        print(colored(f'[+] {tgtPort}/tcp Open', 'green'))
    except:
        print(colored(f'[-] {tgtPort}/tcp Closed', 'red'))
    finally:
        sock.close()
        # closes the remote host connection and releases all managed and unmanaged resources associated with the Socket


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost) # returns a pointer to a hostent structure
    except:
        print(f'Uknown Host {tgtHost}')
    try:
        tgtName = gethostbyaddr(tgtIP) # get the hostname of a specified IP address 
        print(colored('[+] Scan results for: ' + tgtName[0], 'blue'))

    except:
        print(colored('[+] Scan results for: ' + tgtIP, 'yellow'))

    # settimeout(1)
    for tgtPort in tgtPorts:
        thread = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        #The thread class requires a target and an argument
        thread.start()


def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H ,target host. -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()
    # of the options, take the argument and package the arguments 
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        # when there is a need to represent input data from source code abstractly as a 
        # data structure so that it can be checked for the correct syntax
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()