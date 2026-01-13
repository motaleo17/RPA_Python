import sys
import time
import pyautogui
from datetime import datetime
from PIL import ImageGrab

class BMLock:

    def __init__(self, pause=0.5):
        pyautogui.PAUSE = pause
        pyautogui.FAILSAFE = True

    def BMLocate(self, template_path, confidence=0.8):
        try:
            return pyautogui.locateCenterOnScreen(
                template_path,
                confidence=confidence
            )
        except Exception:
            return None
        
    def BMScreenshot():
        print("__SCREENSHOT__", flush = True)
        time.sleep(3)

    def BMClick(self, template_path, timeout=10):
        start = time.time()
        while time.time() - start < timeout:
            pos = self.BMLocate(template_path)
            if pos:
                pyautogui.click(pos)
                return True
            time.sleep(0.5)
        return False

    def BMLocalshot():
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        path = f"C:/Lighthouse/Screenshots/{now}.jpg"
        ImageGrab.grab().save(path)
        print("__LOCALSHOT__" + path, flush=True)
