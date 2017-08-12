#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: entertainment_center.py.py
@time: 8/11/17 3:34 PM
"""

import media,fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

game_of_thrones = media.TvShow("Game of Thrones",
                               "An American fantasy drama television series created by David Benioff and D. B. Weiss.",
                               "https://upload.wikimedia.org/wikipedia/en/0/04/Game_of_Thrones_Season_7.jpg",
                               "https://www.youtube.com/watch?v=giYeaKsXnsI",
                               7,
                               4,
                               "HBO")

secret_forest = media.TvShow("Stranger",
                             "a South Korean television series starring Jo Seung-woo and Bae Doo-na.",
                             "https://upload.wikimedia.org/wikipedia/en/d/d8/Stranger_Poster.jpg",
                             "https://youtu.be/xUOSR7GDCqY",
                             1,
                             2,
                             "tvN")


videos = [toy_story,avatar,game_of_thrones,secret_forest]
fresh_tomatoes.open_movies_page(videos)

# print media.Movie.valid_rating
# print media.Movie.__doc__ #  >> This class provides a way to store movie related information
# print media.Movie.__module__ # media
# print media.Movie.__name__   # Movie


# game_of_thrones.show_trailer()
