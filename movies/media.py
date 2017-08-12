#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: media.py
@time: 8/11/17 3:32 PM
"""
import webbrowser

class Video():
    def __init__(self, title, duration):
        print "Video Constructor is called."
        self.title = title
        self.duration = duration


class Movie(Video):
    """ This class provides a way to store movie related information"""
    valid_rating = ["G","PG","PG-13","R"] # Class Variable

    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        print "Movie Constructor is called."
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



class TvShow(Movie):
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube,season, episode, tv_station):
        print "TvShow Constructor is called."
        Movie.__init__(self,movie_title, movie_storyline, poster_image, trailer_youtube)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        pass