#!/usr/bin/env python

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))

import sqlite3
import Definitions
from blindcontroller import Blindcontroller

'''
Created on 16.08.2013
Einfache Aktion, die auf GET-Anfragen die Datenbank anpasst
'''

#print os.environ.keys()
parameter, value = os.environ.get('QUERY_STRING', "FAIL").split("=")
name, id = parameter.split("-")


mapping = {'mode': 'mode', 'position': 'targetposition', 'sunrise': 'sunrisedelay', 'sunset': 'sunsetdelay'}
if mapping.has_key(name):
    conn = sqlite3.connect(Definitions.DATABASE_FILEPATH)
    c = conn.cursor()
    execStr = '''UPDATE blinds SET %s=%s WHERE id=%s;''' % (mapping.get(name), "'" + value + "'", id)
    c.execute(execStr)
    conn.commit()
    conn.close()
        

print """Content-type: text/plain"""
print
print """done %s""" % ("asdf")
