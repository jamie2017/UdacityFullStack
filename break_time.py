#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: break_time.py
@time: 8/11/17 1:24 PM
"""
import webbrowser

import time


class break_time(object):
    def open_browser(self, url):
        webbrowser.open(url)

    def take_a_break(self,url, lasting = 120):
        print "This program start at ", time.ctime()
        total_breaks = 3
        break_count = 0
        while break_count < total_breaks:
            self.open_browser(url)
            break_count += 1
            time.sleep(lasting)


def Main():
    test = break_time()
    test.take_a_break("https://www.youtube.com/watch?v=SLSjqCPkdWA")

if __name__ == "__main__":
    Main()