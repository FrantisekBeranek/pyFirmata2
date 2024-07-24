from .constants import *
from .util import to_two_bytes
from time import time, sleep

'''
Extends standard pyFirmata2 library with I2C bus.
'''

I2C_WRITE           = 0
I2C_READ            = 1
I2C_READ_CONTINOUS  = 2
I2C_STOP_READING    = 3

class AddressOutOfRange(Exception):
    pass

class ReadTimeout(Exception):
    pass

class I2C(object):
    """ Object for i2c bus handling """

    def __init__(self, board, sda, scl):
        self._board = board
        self._buff = []
        self._sda = sda
        self._scl = scl

    def config(self, delay = 0):
        msg = to_two_bytes(delay)
        self._board.send_sysex(I2C_CONFIG, msg)

    def request(self, add:int, r_w:int, data:bytearray, add_mode = False):
        if add > 1024 | ((add > 256) & (add_mode == False)):
            raise AddressOutOfRange("Address of I2C slave is out of range")
        if add_mode == True:
            add |= (1<<13)
        add |= (r_w<<11)
        msg = [add & 0xFF, add >> 8]
        for d in data:
            msg.extend(to_two_bytes(d))
        self._board.send_sysex(I2C_REQUEST, msg)
        sleep(0.5)

    def available(self):
        return len(self._buff)

    def write_byte(self, add:int, data:int, add_mode = False):
        self.request(add, I2C_WRITE, [data], add_mode)

    def write_block(self, add:int, data:bytearray, add_mode = False):
        self.request(add, I2C_WRITE, data, add_mode)

    def read(self):
        if self.available():
            return self._buff.pop(0)
    
    def read_block_from(self, add, offset, length, timeout=10, add_mode = False):
        if offset == None:
            data = [length]
        else:
            data = [offset, length]
        self.request(add, I2C_READ, data, add_mode)
        start = time()
        while time() < start+timeout/1000:
            if self.available() == length+2:
                self.read() # first byte is slave address
                self.read() # second byte is register
                msg = []
                for i in range(length):
                    msg.append(self.read())
                return msg
            
        while self.available(): # clear buffer
            self.read()
        raise ReadTimeout("I2C reading timeout")

    def read_from(self, add, offset=None, timeout=10, add_mode = False):
        ret = self.read_block_from(add, offset, 1, timeout, add_mode)   # returns list
        return ret[0]
    