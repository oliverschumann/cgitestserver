#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

#import Definitions
#import sqlite3


statusPageHtml = """
    <div data-role="page" id="status">
        <div data-role="header">
            <h1>Heizung - Übersicht</h1>
            <a href="#configuration" data-icon="gear" class="ui-btn-right" data-iconpos="notext"></a>
        </div><!-- /header -->
    
        <div data-role="content">
        
        
        <ul data-role="listview" data-inset="true">
            <li data-role="list-divider">Temperaturen</li>
            <li>
                <div class="ui-grid-a">
                    <div class="ui-block-a">
                        Außen: <span class="gridspanRight">17.8°</span> 
                    </div>
                    <div class="ui-block-b">
                        Innen: <span class="gridspanRight">21.8°</span> 
                    </div>
                </div><!-- /grid-a -->
            </li>
            
               
            
            <li>
                <div class="ui-grid-a">
                    <div class="ui-block-a">
                        Brauchwasser: <span class="gridspanRight">35.6°</span>
                    </div>
                    <div class="ui-block-b">
                        Kessel:<span class="gridspanRight">43.8°</span><br />
                        Kesselziel:<span class="gridspanRight">51.0°</span><br />
                    </div>
                </div><!-- /grid-a -->
            </li>

            
            <li>
                <div class="ui-grid-a">
                    <div class="ui-block-a">
                        EG-V:<span class="gridspanRight">43.8°</span><br />
                        EG-R:<span class="gridspanRight">18.0°</span><br />
                    </div>
                    <div class="ui-block-b">
                        OG-V:<span class="gridspanRight">43.8°</span><br />
                        OG-R:<span class="gridspanRight">21.0°</span><br />
                    </div>
                </div><!-- /grid-a -->
            </li>
            
            <li>
                <div class="ui-grid-solo">
                    <div class="ui-block-a">
                        <a data-role="button" data-icon="refresh" data-iconpos="top" href="#">Aktualisieren</a>
                    </div>
                </div>
                <div class="ui-grid-a">
                    <div class="ui-block-a">
                        <a data-role="button" href="#">Brauchwasser</a>
                        <a data-role="button" href="#">Zirkulationspumpe</a>
                    </div>
                    <div class="ui-block-b">
                        <a data-role="button" href="#">Erdgeschoss</a>
                        <a data-role="button" href="#">Obergeschoss</a>
                    </div>
                </div><!-- /grid-a -->
            </li>
            
        </ul>
        <ul data-role="listview" data-inset="true">
            
            <li data-role="list-divider">Pumpen</li>
            <li>
                <div class="ui-grid-a">
                    <div class="ui-block-a">
                        Brauchwasser: <span class="gridspanRight">an</span> <br />
                        Zirkulation: <span class="gridspanRight">an</span> 
                    </div>
                    <div class="ui-block-b">
                        Fussboden: <span class="gridspanRight">an</span> <br />
                        Obergeschoss: <span class="gridspanRight">an</span> 
                    </div>
                </div><!-- /grid-a -->
            </li>
        </ul>
        
        
        </div><!-- /content -->
        
    </div><!-- /page -->
"""

# Ausgabe# Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe  
# Ausgabe# Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe  
# Ausgabe# Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe # Ausgabe
  
print """Content-type: text/html; charset=utf-8"""
print
print """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Heizung</title>
        <link rel="stylesheet"  href="../files/css/themes/default/jquery.mobile-1.3.2.min.css">
        
        <script src="../files/js/jquery.js"></script>
        <script src="../files/js/jquery.mobile-1.3.2.min.js"></script>
        <style>
        .gridspanRight {
            float: right;
            margin-right: 15px;
        }
        </style>
    </head>
    <body>   
"""
#CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT

print statusPageHtml

#CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT

print """
    </body>
</html>
"""

a = """
 <div class="ui-grid-a">
                    <div class="ui-block-a">
                    </div>
                    <div class="ui-block-b">
                    </div>
                </div>
"""