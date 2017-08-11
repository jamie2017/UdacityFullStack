#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: media.py
@time: 8/11/17 3:32 PM
"""
import webbrowser


class Movie(object):
    """ This class provides a way to store movie related information"""
    valid_rating = ["G","PG","PG-13","R"] # Class Variable

    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


