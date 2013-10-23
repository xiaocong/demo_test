#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uiautomator import device as d
import os

def settings():
    if d(text='设置').exists:
        d(text='设置').click()
        d.screenshot(os.path.join(os.environ.get('WORKSPACE', '.'), 'screenshot.png'))
        d.press.back()

for i in range(20):
    d.screen.on()
    print("Swipe left")
    d().swipe.left()
    print("Swipe right")
    d().swipe.right()
    d.press.home()
    settings()
