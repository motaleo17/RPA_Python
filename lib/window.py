from pywinauto import Desktop
import time

class WindowManager:

    @staticmethod
    def wait(title, timeout=10):
        end = time.time() + timeout
        while time.time() < end:
            try:
                win = Desktop(backend="uia").window(title=title)
                if win.exists():
                    win.set_focus()
                    return win
            except:
                pass
            time.sleep(0.5)
        return None
