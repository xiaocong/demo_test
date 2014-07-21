#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uiautomator import device as d
import os

def loop(texts):
    for view in d():
        text = view.text
        if text and text not in texts:
            d(text=text).click()
            d.press.back()
            texts.append(text)
            return True
    else:
        return False

def main():
    texts = []
    d(scrollable=True).scroll.horiz.toBeginning()
    while d(scrollable=True).scroll.horiz.forward(steps=10):
        while loop(texts):
            pass

if __name__ == '__main__':
    for i in range(100000):
        main()
