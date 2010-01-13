
class TimeoutError(Exception):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        "Return a string representation of the exception"
        return str(self.value)
