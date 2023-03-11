"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start_num):
        """Saves the passed in number to the start_num variable and into the original_num variable for later use after start_num is changed"""
        self.start_num = start_num
        self.original_num = start_num

    def __repr__(self):
        """returns the current serial number and the following serial number"""
        return f"SerialGenerator start = {self.start_num} next = {self.start_num + 1}"

    def generate(self):
        """Adds 1 to the serial number consecutively"""
        self.start_num += 1
        return self.start_num

    def reset(self):
        """Resets the start_num back to the orignially passed in start_num using original_num"""
        self.start_num = self.original_num
        return self.start_num
