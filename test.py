from uiautomator import device as d

for i in range(1000):
    d.screen.on()
    print("Swipe left")
    d().swipe.left()
    print("Swipe right")
    d().swipe.right()
    d.press.home()
