#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uiautomator import device as d
import os
import time

def main():
    d().scroll.horiz.toBeginning()
    pre = None
    while d(focused=True).exists:
        cur = d(focused=True).info
        print cur['text']
        if cur == pre:
            break
        else:
            pre = cur
        d(focused=True).click()
        time.sleep(3)
        d.press.home()
        time.sleep(3)
        d.press.right()
        time.sleep(3)
        
            
if __name__ == '__main__':
    for i in range(100000):
        main()
