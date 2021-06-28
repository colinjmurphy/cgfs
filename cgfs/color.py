class Color:
    def __init__(self, red: int, green: int, blue: int):
        self._red = red
        self._green = green
        self._blue = blue

    def __bytes__(self):
        return bytes((self._red, self._green, self._blue))
