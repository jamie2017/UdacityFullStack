#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Jianmei Ye
@file: DrawShape.py
@time: 8/11/17 2:18 PM
"""
import turtle



class DrawShape(object):
    def draw_square(self,some_turtle):
        for i in range(4):
            some_turtle.forward(100)
            some_turtle.right(90)

    def draw_art(self):
        window = turtle.Screen()
        window.bgcolor("blue")
        brad = turtle.Turtle()
        brad.shape("turtle")
        brad.color("yellow")
        brad.speed(2)
        self.draw_square(brad)

        angie = turtle.Turtle()
        angie.shape("arrow")
        angie.color("red")
        angie.circle(100)
        window.exitonclick()

    def draw_circle_by_square(self):
        window = turtle.Screen()
        window.bgcolor("blue")
        brad = turtle.Turtle()
        brad.shape("turtle")
        brad.color("yellow")
        brad.speed(5)
        total_degree = 360
        while total_degree > 0:
            self.draw_square(brad)
            brad.right(10)
            total_degree -= 10
        window.exitonclick()





def Main():
    test = DrawShape()
    test.draw_circle_by_square()

if __name__ == "__main__":
    Main()