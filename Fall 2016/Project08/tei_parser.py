# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:58:04 2016

This code encapsulates TEI format parsing details. It simply extracts pairs of
word/translation from the file and return them piled up as a list of tuples.

@author: Haitham Seada
"""

import xml.sax

"""
This class represents a TEI XML parser. It can pulls information from the TEI
file into a list of tuples. Each tuple contains two values, the first value
is the original word while the second value is its translation.
"""
class TeiHandler( xml.sax.ContentHandler ):

    # Initializations
    def __init__(self):
        # The list of tuples each in the form (word,translation)
        self.transLst = []
        # The last open TAG
        self.currentTag = ""
        # The current original word (to be translated)
        self.word = ""
        # The translation of the current original word
        self.translation = ""
        # Utility fileds
        self.entryStarted = False
        self.transExpected = False
        
    # Call when an element starts
    def startElement(self, tag, attributes):
        self.currentTag = tag
        if tag == "entry":
            self.entryStarted = True
        elif tag == "cit":
            if attributes["type"] == "trans":
                self.transExpected = True

    # Call when an elements ends
    def endElement(self, tag):
        if tag == "entry":
            # If you have a word and a translation (non of them is empty)
            if self.word and self.translation:
                # Avoid phrases (the file has some whole-phrase tarnslations)
                if len(self.word.split()) == 1:
                    self.transLst.append((self.word, self.translation))
            # Reset your variables
            self.word = ""
            self.translation = ""
            self.entryStarted = False
        # Reset your current tag
        self.currentTag = ""

    # Call when a character is read
    def characters(self, content):
        if self.currentTag == "orth" and self.entryStarted:
            # Capture the original word
            self.word = content.strip().lower()
        elif self.currentTag == "quote" and self.transExpected:
            # Capture the translation
            self.translation = content.strip()
            self.transExpected = False

"""
This function takes the name of the TEI file and returns a list of tuples
each containing the translation of a single word. Notice that although this
function pulls translations of single words only (not multi-word phrases),
the translation can have more than one word.
"""
def parseTeiFile(fileName):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler
    handler = TeiHandler()
    parser.setContentHandler(handler)
    # Return the final translation list of tuples
    parser.parse(fileName)
    return handler.transLst