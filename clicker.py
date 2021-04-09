import pyautogui

clicks = 10

try:
    X, Y = pyautogui.locateCenterOnScreen("gen_1000_samples.png")
    pyautogui.click(X, Y, clicks=clicks, interval=0.25)
    print(f"{clicks*1000} samples generated!")

except Exception:
    print("Button not found. Adjust Statkey screen.")

