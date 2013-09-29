# -*- coding: utf-8 -*-
'''
Created on 16.08.2013
@author: Oliver Schumann
'''
import time

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

class RequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
    pass
    #def log_message( self, format, *args ):
    #    pass


                 
def startCgiHttpServer():
    server = BaseHTTPServer.HTTPServer
    handler = RequestHandler
    server_address = ("", 8000)
    handler.cgi_directories = ['/cgi-bin']
    
    httpd = server(server_address, handler)
    httpd.serve_forever()


if __name__ == '__main__':
    startCgiHttpServer()
    while True:
        time.sleep(60)
    pass