import pyautogui

clicks = 10  # left click 10 times
interval = 0.25  # delay clicks by 0.25sec

try:
    X, Y = pyautogui.locateCenterOnScreen("gen_1000_samples.png")
    pyautogui.click(X, Y, clicks=clicks, interval=interval)
    print(f"{clicks*1000} samples generated!")

except Exception:
    print("Button not found. Adjust Statkey screen.")
