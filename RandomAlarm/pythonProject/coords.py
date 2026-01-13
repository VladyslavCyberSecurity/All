import pyautogui
import time

print("Наведи мишку на будь-яке місце... (Ctrl + C для виходу)")

while True:
    x, y = pyautogui.position()
    print(x, y)
    time.sleep(1)
