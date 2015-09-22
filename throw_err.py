#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys, os

class NoClass(object):
    pass

def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.exit()

def assertionErr(x):
    assert (x>0), '%s is not greater than 0!?' % (x)
    return (x)

def ioErr():
    name = '/no_such_file.txt'
    with open("no_such_file.txt") as f:
        print(f.readline())

def importErr():
    from abcde import fghij
    
def indexErr():
    a=[1,2,3]
    return a[4]

def keyErr():
    a = { 'there':1, 'iz':2, 'no':3, 'spoon':4 }
    print a['illusion']

def nameErr():
    if trolololol < 777:
        return trolololol-77

def osErr():
    for i in range(10):
        print i, os.ttyname(i)

def typeErr():
    name = 'fantastico'
    return name + 3

def valueErr():
    print chr(1024)

def zerodivErr(x):
    return x/0 

def attributeErr():
    scrub = NoClass()
    print scrub.Money

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    assertionErr(-7)
elif error_type == "io":
    ioErr()
elif error_type == "import":
    importErr()
elif error_type == "index":
    indexErr()
elif error_type == "key":
    keyErr()
elif error_type == "name":
    nameErr()
elif error_type == "os":
    osErr()
elif error_type == "type":
    typeErr()
elif error_type == "value":
    valueErr()
elif error_type == "zerodivision":
    zerodivErr(7)
elif error_type == "attribute":
    attributeErr()
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
