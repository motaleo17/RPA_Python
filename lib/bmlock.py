import sys
import time
import cv2
import numpy as np
import pyautogui
from PIL import Image
import pyscreenshot as ImageGrab
from datetime import datetime
sys.stdout.flush()

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )
    return thresh
    
def BMLocate(template_path, threshold=0.75):
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_path)
    screen_p = preprocess_image(screen)
    template_p = preprocess_image(template)
    result = cv2.matchTemplate(screen_p, template_p, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        h, w = template_p.shape
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y)
    return None
    
def BMClick(template_path, timeout=10):
    start = time.time()
    while time.time() - start < timeout:
        pos = BMLocate(template_path)
        if pos:
            pyautogui.click(pos)
            return True
        time.sleep(0.5)
    return False


def BMScreenshot():
    print("__SCREENSHOT__", flush = True)
    time.sleep(3)

def BMSetVar(key,value):
    print("__SET__" + key + "=" + str(value), flush = True)

def BMLogMessage(msg):
    print(msg, flush = True)
    
def BMLocalshot():
    now = datetime.now()
    current_date = now.strftime("%Y%m%d%H%M%S")
    imagePath = "C:/Lighthouse/Screenshots/"+current_date+" .jpg"
    screenshot = ImageGrab.grab()
    screenshot.save(imagePath,"jpeg")
    print("__LOCALSHOT__"+imagePath, flush = True)
    time.sleep(5)