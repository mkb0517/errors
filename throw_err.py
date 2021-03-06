#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys, os, math, gc, weakref, argparse

available_errors = ["assertion", "io", "import", "index", "key", "name", "os",
    "type", "value","zerodivision", "attribute", "unbound", "reference", 
    "overflow", "unimportant"]
parser = argparse.ArgumentParser()
parser.add_argument("error_type",
    choices=available_errors)
args = parser.parse_args()
error_type = args.error_type

class Scrub(object):
    pass

class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print '(Deleting %s)' % self

class UnimportantError:
    """Everything is just so... bleh"""

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
    for i in range(7):
        print i, os.ttyname(i)

def typeErr():
    name = 'fantastico'
    return name + 3

def valueErr():
    print chr(257)

def zerodivErr(x):
    return x/0 

def attributeErr():
    scrub = Scrub()
    print scrub.Money

def refErr():
    laptop = ExpensiveObject('cost so much!')
    p = weakref.proxy(laptop)

    print 'BEFORE:', p.name
    laptop = None
    print 'AFTER:', p.name

def unboundErr():
    local_val = local_val + 1
    print local_val

def overflowErr():
    print 2.0**1000000

def unimpErr():
    crumb = "meh"
    if crumb != "ZOMG WOW": 
        raise UnimportantError

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
elif error_type == "reference":
    refErr()
elif error_type == "unbound":
    unboundErr()
elif error_type == "overflow":
    overflowErr()
elif error_type == "unimportant":
    unimpErr()

else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
