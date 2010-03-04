import sys
import markov
import os
import random

class Enpersonator:
    STOP = "_meta_end_dot_"

    filespaths = ['blog_data_v1_0/cb/distilled/data/bodies_distiled',
                  'blog_data_v1_0/dk/distilled/data/bodies_distiled',
                  'blog_data_v1_0/my/distilled/data/bodies_distiled',
                  'blog_data_v1_0/rs/distilled/data/bodies_distiled',
                  'blog_data_v1_0/rwn/distilled/data/bodies_distiled']

    lines = []
    #thetext = ""

    def __init__(self):
        print "ENP> Initializing Enpersonator"
        self.parseData()
        
    def replaceEvery(self, thisText, replaceThis):
        #print "replaceEvery: ",thisText.count(replaceThis)
        for i in range(thisText.count(replaceThis)):
            #print i,": Replacing ",replaceThis
            thisText = thisText.replace(replaceThis, self.randomNumberString(10, 500), 1)
        #print "new: ",thisText
        return thisText

    def randomNumberString(self, start, end):
        return str(random.randint(start, end))

    def parseData(self):
        print "ENP> Parsing Data"
        for thisPath in self.filespaths:
            files = []
            for thisFile in os.listdir(thisPath):
                if(thisFile[0] != '.'):
                    files.append(thisFile)

            for thisFile in files:
                f = open(thisPath + "/" + thisFile, 'r')
                thetext = f.read()
                # Clean up shitty formatting
                thetext = thetext.replace(" s ", "'s ")
                thetext = thetext.replace(" t ", "'t ")
                thetext = thetext.replace(" m ", "'m ")
                thetext = thetext.replace(" i ", " I ")
                thetext = thetext.replace(" i'", " I'")
                thetext = thetext.replace(" ve ","'ve ")
                thetext = thetext.replace(" ll ","'ll ")
                thetext = thetext.replace("e mail","'email")
                thetext = thetext.replace("\r\n"," ")
                thetext = thetext.replace(" re ", "'re ")
                thetext = thetext.replace(" _meta_end_exclamation_", "!")
                thetext = thetext.replace("\n"," ")
                thetext = thetext.replace(" _meta_end_question_", "?")
                thetext = thetext.strip()
                self.lines.extend(thetext.split(self.STOP))
        print "ENP> Done parsing. Using ",len(self.lines)," words of source text."
        
    def generateLine(self, order=2, max=200):

        gen = markov.MarkovGenerator(order, max)
        print "ENP> Feeding Analyzer"
        for line in self.lines:
            line = line.strip()
            gen.feed(line)

        newLine = gen.generate()

        newLine = self.replaceEvery(newLine, "_meta_number_ref_")
        newLine = self.replaceEvery(newLine, "_meta_dollor_ref_")
        newLine = self.replaceEvery(newLine, "_meta_percent_ref_")
        
        return newLine
