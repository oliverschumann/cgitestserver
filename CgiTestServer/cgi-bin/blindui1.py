# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

#import Definitions
#import sqlite3

print """Content-type: text/html; charset=utf-8"""
print
print """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Rollo</title>
    <link rel="stylesheet"  href="../files/css/themes/default/jquery.mobile-1.3.2.min.css">
    
    <script src="../files/js/jquery.js"></script>
    <script src="../files/js/jquery.mobile-1.3.2.min.js"></script>
</head>
<body>
    <div data-role="page" id="control">
        <div data-role="header">
            <h1>Rollos</h1>
            <a href="#configuration" data-icon="gear" class="ui-btn-right" data-iconpos="notext"></a>
        </div><!-- /header -->
    
        <div data-role="content">
"""
#CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT

print """
<ul data-role="listview" data-inset="true" data-divider-theme="d">
    <li data-role="list-divider">Wohnzimmer</li>
    <li>
        <div class="ui-grid-solo">
            <div class="ui-block-a">
                <form>
                    <fieldset data-role="controlgroup" data-type="horizontal">
                        <input type="checkbox" name="checkbox-h-2a" id="checkbox-h-2a" checked="checked">
                        <label for="checkbox-h-2a"> 1 </label>
                        <input type="checkbox" name="checkbox-h-2b" id="checkbox-h-2b" checked="checked">
                        <label for="checkbox-h-2b"> 2 </label>
                        <input type="checkbox" name="checkbox-h-2c" id="checkbox-h-2c" checked="checked">
                        <label for="checkbox-h-2c"> 3 </label>
                        <input type="checkbox" name="checkbox-h-2d" id="checkbox-h-2d" checked="checked">
                        <label for="checkbox-h-2d"> 4+5 </label>
                    </fieldset>
                </form>
            </div>
        </div>
        <div class="ui-grid-b">
            <div class="ui-block-a"><a data-role="button" data-icon="arrow-u" data-iconpos="top" href="#">Auf</a></div>
            <div class="ui-block-b"><a data-role="button" data-icon="delete" data-iconpos="top" href="#">Stop</a></div>
            <div class="ui-block-c"><a data-role="button" data-icon="arrow-d" data-iconpos="top" href="#">Ab</a></div>
        </div>
    </li>
    <li data-role="list-divider">Küche</li>
    <li>
        <div class="ui-grid-b">
            <div class="ui-block-a"><a data-role="button" data-icon="arrow-u" data-iconpos="top" href="#">Auf</a></div>
            <div class="ui-block-b"><a data-role="button" data-icon="delete" data-iconpos="top" href="#">Stop</a></div>
            <div class="ui-block-c"><a data-role="button" data-icon="arrow-d" data-iconpos="top" href="#">Ab</a></div>
        </div>
    </li>
    <li data-role="list-divider">Schlafzimmer</li>
    <li>
        <div class="ui-grid-b">
            <div class="ui-block-a"><a data-role="button" data-icon="arrow-u" data-iconpos="top" href="#">Auf</a></div>
            <div class="ui-block-b"><a data-role="button" data-icon="delete" data-iconpos="top" href="#">Stop</a></div>
            <div class="ui-block-c"><a data-role="button" data-icon="arrow-d" data-iconpos="top" href="#">Ab</a></div>
        </div>
    </li>
</ul>


"""

#CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT
print """
     </div><!-- /content -->
    </div><!-- /page -->
    
    
    <div data-role="page" id="configuration">
        <div data-role="header">
            <a href="#control" data-rel="back" data-icon="arrow-l class="ui-btn-left" data-iconpos="notext"></a>
            <h1>Konfiguration</h1>
        </div><!-- /header -->
    
        <div data-role="content">
"""
#CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT

print """
"""

#CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT--CONTENT

print """
 </div><!-- /content -->
    </div><!-- /page -->    
</body>
</html>
"""

