from uiautomator import device as d

for i in range(1000):
    d.screen.on()
    d.screen.off()
    d().swipe.left()
    d().swipe.right()
    d.press.home()
