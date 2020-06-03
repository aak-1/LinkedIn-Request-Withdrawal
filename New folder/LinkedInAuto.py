import pyautogui, time, os, webbrowser
page = input('enter page number')
chromedir = '<insert chrome.exe address> %s'
webbrowser.get(chromedir).open(f"https://www.linkedin.com/mynetwork/invitation-manager/sent/?invitationType=&page={page}")

#pyautogui.FAILSAFE = True
#time.sleep(1)

time.sleep(5)

for o in range(0,10):
    time.sleep(0.3)
    x, y = pyautogui.locateCenterOnScreen("withdraw1.PNG", confidence=0.7)
    pyautogui.click(x,y)
    time.sleep(0.5)
    a, b = pyautogui.locateCenterOnScreen('withdraw2.png', confidence=0.7)
    pyautogui.click(a,b)
    #pyautogui.press('enter')
