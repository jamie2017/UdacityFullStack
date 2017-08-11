#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: CheckProfanity.py
@time: 8/11/17 3:12 PM
"""
import urllib


class CheckProfanity(object):
    def read_text(self):
        quotes = open("/Users/JMYE/Documents/Python/UdacityFullStack/ProfanityEditor/quotes.txt")
        contents_of_file = quotes.read()
        print contents_of_file
        quotes.close()
        self.check_profanity(contents_of_file)

    def check_profanity(self, text_to_check):
        connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
        output = connection.read()
        connection.close()
        if "true" in output:
            print "Profanity Alert!"
        elif "false" in output:
            print "No Profanity Detected!"
        else:
            print "Could not scan the document properly."

def Main():
    test = CheckProfanity()
    test.read_text()


if __name__ == "__main__":
    Main()