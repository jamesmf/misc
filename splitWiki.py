# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 15:38:39 2015

@author: frickjm
"""

storedPage  = ""
title       = ""

with open("../../../prod/peryeata/wiki/enwiki-20150403-pages-meta-current.xml",'rb') as f:
    for line in f:
        if line.find("<text") > -1:
            inContent   = True
        if inContent:
            storedPage  += line
        if line.find("<title>") > -1:
            title   = line[line.find("title")+6:line.find("</title")]
        if line.find("</text") > -1:
            print title
            print storedPage
            stop    = raw_input("")
            inContent   = ""
            title       = ""
            storedPage  = ""