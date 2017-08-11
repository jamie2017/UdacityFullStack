#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: SendSecretMsg.py
@time: 8/11/17 1:43 PM
"""
import os

class SendSecretMsg(object):
    def rename_file(self):
        file_path = "/Users/JMYE/Documents/Python/UdacityFullStack/SendSecretMsg/prank"
        file_list = os.listdir(file_path)
        os.chdir(file_path)
        for filename in file_list:
            if ".jpg" not in filename:
                continue
            os.rename(filename, self.remove_digit(filename))

        file_list = os.listdir("/Users/JMYE/Documents/Python/UdacityFullStack/SendSecretMsg/prank")
        print file_list



    def remove_digit(self,filename):
        #     "".join([c for c in filename if not c.isdigit()])
        return filename.translate(None, "0123456789")



def Main():
    test = SendSecretMsg()
    test.rename_file()

if __name__ == "__main__":
    Main()