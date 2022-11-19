"""Python serial number generator."""

class SerialGenerator():
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

    def __init__(self, start):
        '''Initialize SerialGenerator instance with start number, and an offset of zero'''
        self.start = start
        self.offset = -1
    
    def generate(self):
        '''Generate a serial number using the start and offset attr on self'''
        self.offset += 1
        return self.start + self.offset

    def reset(self):
        '''Reset the serial number generator offset to 0'''
        self.offset = -1