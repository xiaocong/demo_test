#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uiautomator import device as d
import os

def loop(texts):
    for view in d():
        if view.text:
            d(text=view.text).click()
            d.press.back()

def main():
    texts = []
    d(scrollable=True).scroll.horiz.toBeginning()
    while d(scrollable=True).scroll.horiz.forward(steps=10):
        loop(texts)

if __name__ == '__main__':
    for i in range(100000):
        main()
