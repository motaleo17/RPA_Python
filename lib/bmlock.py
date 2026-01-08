import sys
import time
import cv2
import numpy as np
import pyautogui
from PIL import Image
import pyscreenshot as ImageGrab
from datetime import datetime

class BMLock:

    def __init__(self, pause=0.5):
        self.pause = pause
        pyautogui.PAUSE = pause
        pyautogui.FAILSAFE = True
        sys.stdout.flush()

    # -------------------------
    # Image helpers
    # -------------------------

    def _preprocess_image(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(
            blur, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )
        return thresh

    # -------------------------
    # Public API (mantém nomes)
    # -------------------------

    def BMLocate(self, template_path, threshold=0.75):
        screen = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

        template = cv2.imread(template_path)
        if template is None:
            return None

        screen_p = self._preprocess_image(screen)
        template_p = self._preprocess_image(template)

        result = cv2.matchTemplate(
            screen_p,
            template_p,
            cv2.TM_CCOEFF_NORMED
        )

        _, max_val, _, max_loc = cv2.minMaxLoc(result)
