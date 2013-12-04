#! /usr/bin/env python
import sys
import re
import os
from optparse import OptionParser




#work with the files

def get_file(thisdir):
    """docstring for get_file
    gets files from directory"""
    with open(thisdir, 'r') as f:
        return f.read()
        
def keyword_regex(words):
    """docstring for keyword_regular"""
    searches={}
    for word in words:
        searches[word]=re.compile(r'\b' + word + r'\b', re.IGNORECASE)
    return searches
        
def count_keywords(searches,text):
    """docstring for count_keywords"""
    for kw in searches:
        print "\"{0}\": {1}".format(kw, len(re.findall(searches[kw], text)))
    print '\n\n'     
    
def metadata(full_text,file):
    """docstring for metadata"""
    title_search = re.compile(r'(title:\s*)(?P<title>(.*)[]*?\n[]*(.*))', re.IGNORECASE|re.VERBOSE)
    author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
    translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
    illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
    
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

    
    
def split_callback(option,opt,value,parser):
    """splits the arguments into a list"""
    setattr(parser.values, option.dest, value.split(','))

def main():
    """lists options and calls other functions"""
    choices=OptionParser()
    choices.add_option("-k", "--keyword",dest="words",type="string", action='callback',callback=split_callback)
    choices.add_option("-d", "--directory",dest="directory",type="string")
    (options, args)=choices.parse_args()

    #error if it data not there
    if not (options.words and options.directory):
        choices.error("You need a directory and some keywords")
    
    txtfiles=os.listdir(options.directory)
    searches=keyword_regex(options.words)
    for file in txtfiles:
        thefile=os.path.join(options.directory, file)
        full_text=get_file(thefile)
        metadata(full_text,file)
        count_keywords(searches,full_text)
if __name__ == '__main__':
    main()
    

