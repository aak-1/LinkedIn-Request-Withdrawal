import pyautogui, time
#pyautogui.FAILSAFE = True
#time.sleep(1)
while True:
    x, y = pyautogui.locateCenterOnScreen("C:\\Users\\hp\\Desktop\\Newfolder\\withdraw1.PNG", confidence=0.8)
    pyautogui.click(x,y)
    time.sleep(0.015)
    a, b = pyautogui.locateCenterOnScreen('C:\\Users\\hp\\Desktop\\Newfolder\\withdraw2.png', confidence=0.8)
    pyautogui.click(a,b)
    #pyautogui.press('enter')