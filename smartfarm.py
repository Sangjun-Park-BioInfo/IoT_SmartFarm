import time
from module import led
#from module import dht
'''import dht
import spi
import heat
import hum
import led
import cam'''


led = led.led()

class smartfarm:
    def __init__(self, day=10):
        self.day = day
        '''self.dht = dht
        self.spi = spi
        self.heat = heat
        self.hum = hum
        self.led = led
        self.cam = cam'''
        

        led.operate(8, 19)
        


if __name__ == "__main__":
    smartfarm()



