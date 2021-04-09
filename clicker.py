import pyautogui


try:
    X, Y = pyautogui.locateCenterOnScreen("gen_1000_samples.png")
    pyautogui.click(X, Y, clicks=10, interval=0.25)
    print("")

except Exception:
    print("Button not found. Adjust Statkey screen.")

