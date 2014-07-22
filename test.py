#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uiautomator import device as d
import os
import time

def main():
    texts = []
    d().scroll.horiz.toBeginning()
    while d(focused=True).exists and d(focused=True).text not in texts:
        texts.append(d(focused=True).text)
        d(focused=True).click()
        time.sleep(1)
        d.press.back()
        d.press.right()
            
if __name__ == '__main__':
    for i in range(100000):
        main()
