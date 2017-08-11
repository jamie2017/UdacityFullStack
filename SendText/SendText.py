#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: SendText.py
@time: 8/11/17 2:49 PM
"""
import twilio
# https://www.twilio.com/console
class SendText(object):
    def send_text(self):
        from twilio.rest import Client

        # Your Account SID from twilio.com/console
        account_sid = "ACXXXXXXXXXXXXXXXXXXXX"
        # Your Auth Token from twilio.com/console
        auth_token = "7XXXXXXXXXXXXXX"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+14*******",
            from_="+140*******", # Replace with your Twilio number
            body="Hello from Jamie!")

        print(message.sid)


def Main():
    test = SendText()
    test.send_text()


if __name__ == "__main__":
    Main()