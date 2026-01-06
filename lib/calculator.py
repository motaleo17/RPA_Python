class Calculator:
    def __init__(self, window):
        self.window = window

    def press(self, auto_id):
        self.window.child_window(
            auto_id=auto_id,
            control_type="Button"
        ).wait("exists ready", timeout=5).click_input()

    def number(self, n):
        for d in str(n):
            self.press(f"num{d}Button")

    def add(self):
        self.press("plusButton")

    def subtract(self):
        self.press("minusButton")

    def multiply(self):
        self.press("multiplyButton")

    def divide(self):
        self.press("divideButton")

    def equals(self):
        self.press("equalButton")
