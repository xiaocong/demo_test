from uiautomator import device as d

for i in range(20):
    d.screen.on()
    print("Swipe left")
    d().swipe.left()
    print("Swipe right")
    d().swipe.right()
    d.press.home()
