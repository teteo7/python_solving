import pyautogui
import time

for _ in range(0,100):
    #x y

    pyautogui.moveTo(5, 5)
    time.sleep(3)

    pyautogui.moveTo(1600,85)
    pyautogui.click()
    pyautogui.typewrite('A', interval=0.1)
    pyautogui.typewrite(['a', 'b'], interval=0.1)

    print("check")
    # 1당 초
    time.sleep(240)

# pyautogui.moveTo(5,30)
# pyautogui.click()