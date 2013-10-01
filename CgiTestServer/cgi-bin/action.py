#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))

import sqlite3

'''
Created on 16.08.2013
Einfache Aktion, die auf GET-Anfragen die Datenbank anpasst
'''

#print os.environ.keys()
# parameter, value = os.environ.get('QUERY_STRING', "FAIL").split("=")
# name, id = parameter.split("-")


import sys, json

result = {'success':'true','message':'The Command Completed Successfully'};
try:
    myjson = json.load(sys.stdin)
    t = "\n##############--%s--#################\n" % (myjson)
    sys.stderr.write(t)
    t = "\n##############--%s--#################\n" % (myjson['request'])
    sys.stderr.write(t)
    
except:
    pass
# Do something with 'myjson' object

print 'Content-Type: application/json\n\n'
print json.dumps(result)    # or "json.dump(result, sys.stdout)"      

# print """Content-type: text/plain"""
# print
# print """done %s""" % ("asdf")
