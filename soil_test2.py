from pymata4 import pymata4
import time
import signal
import sys
from PyMata.pymata import PyMata

board = pymata4.Pymata4()

analog_pin = 1
digital_pin = 8
flag = False

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!!!!')
    if board is not None:
        board.reset()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
board = PyMata('/dev/ttyACM0')

board.set_pin_mode(13, board.OUTPUT, board.ANALOG)

while True:
    value, timestamp = board.analog_read(analog_pin)
    print(value)
    time.sleep(1)
    if ((value >= 1000) & (flag == False)):
        board.digital_write(13, 1)
        flag = True
        time.sleep(1)
    if ((value < 1000) & (flag == True)):
        board.digital_write(13, 0)
        flag = False
        time.sleep(1)



