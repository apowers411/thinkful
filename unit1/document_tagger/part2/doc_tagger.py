#! /usr/bin/env python
import sys
import re
import os
from optparse import OptionParser

#get input from user
choices=OptionParser()
choices.add_option("-k", "--keyword",dest="words",type="string")
choices.add_option("-d", "--directory",dest="directory",type="string")
(options, args)=choices.parse_args()

#error if it data not there
if not (options.words and options.directory):
    choices.error("You need a directory and some keywords")

#initialize searches
title_search = re.compile(r'(title:\s*)(?P<title>(.*)[]*?\n[]*(.*))', re.IGNORECASE|re.VERBOSE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

#create a dictionary of keyword with value=None
searches={}
searches[options.words]=re.compile(r'\b' + options.words + r'\b', re.IGNORECASE)

#work with the files
txtfiles=os.listdir(options.directory)
for file in txtfiles:
    filetoread=os.path.join(options.directory, file)
    with open(filetoread, 'r') as f:
        full_text=f.read()
    title=re.search(title_search, full_text).group('title')
    author=re.search(author_search, full_text)
    translator=re.search(translator_search,full_text)
    illustrator = re.search(illustrator_search, full_text)
    if author:
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')
    print "***" * 25
    print "Here's the info for doc {}:".format(file)
    print "Title: {}".format(title)
    print "Author(s): {}".format(author)
    print "Translator(s): {}".format(translator)
    print "Illustrator(s): {}".format(illustrator)
    print "\n"
    print "***" * 25
    print "Here's the keyword info for doc {}:".format(file)
    for kw in searches:
        print "\"{0}\": {1}".format(kw, len(re.findall(searches[kw], full_text)))
    print '\n\n'

   

