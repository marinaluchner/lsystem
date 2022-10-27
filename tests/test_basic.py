import pyautogui
print("Basic test running")


x, y = pyautogui.locateCenterOnScreen('calc7key.png')
pyautogui.click(x, y)
