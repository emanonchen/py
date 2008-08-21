# py/pyext - python script objects for PD and MaxMSP
#
# Copyright (c) 2002-2008 Thomas Grill (gr@grrrr.org)
# For information on usage and redistribution, and for a DISCLAIMER OF ALL
# WARRANTIES, see the file, "license.txt," in this distribution.  
#

"""This is an example script for the py/pyext object's buffer support.

Pd/Max buffers can be mapped to Python arrays.
Currently, there are three implementations:
Numeric, numarray and numpy (for all of them see http://numeric.scipy.org)
"""

import sys

try:
    import pyext
except:
    print "ERROR: This script must be loaded by the PD/Max py/pyext external"

try:
    # numpy is assumed here... numeric and numarray are considered deprecated
    from numpy import *
except:
    print "Failed importing numpy module:",sys.exc_value

def mul(*args):
    # create buffer objects
    # as long as these variables live the underlying buffers are locked
    c = pyext.Buffer(args[0])
    a = pyext.Buffer(args[1])
    b = pyext.Buffer(args[2])

    # slicing causes Python arrays (mapped to buffers) to be created
    # note the c[:] - to assign contents you must assign to a slice of the buffer
    c[:] = a[:]*b[:]  

def add(*args):
    c = pyext.Buffer(args[0])
    a = pyext.Buffer(args[1])
    b = pyext.Buffer(args[2])

    # this is also possible, but is probably slower
    # the + converts a into a Python array, the argument b is taken as a sequence
    # depending on the implementation this may be as fast
    # as above or not
    c[:] = a+b  

def fadein(target):
    a = pyext.Buffer(target)
    # in place operations are ok
    a *= arange(len(a),type=Float32)/len(a)

def neg(target):
    a = pyext.Buffer(target)
    # in place transformation (see Python array ufuncs)
    negative(a[:],a[:])
    # must mark buffer content as dirty to update graph
    # (no explicit assignment occurred)
    a.dirty() 
