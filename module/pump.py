import time
from . import spi
import RPi.GPIO as GPIO

now = time.localtime
print("time: %02d:%02d:%02d led: on" % (now.tm_hour,
                        now.tm_min, now.tm_sec))

class pump:

    def __init__(self, moist = 0.14):
        self.status = "off"
        self.moist = moist
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)    
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17, True)

    def on(self):
        GPIO.output(17, False)
        self.status = "on"
    def off(self):
        GPIO.output(17, True)
        self.status = "off"

    def test(self):
        print("Pump test")
        print("pump on")
        self.on()
        time.sleep(5)
        print("pump off")
        self.off()

    def stat(self):
        return self.status

    def operate(self):
        
        while True:
            try:
                spi = spi.spi()    
                moist = spi.measure()
                del spi

                if moist <= self.moist:
                    self.on()
                    print("time: %02d:%02d:%02d pump: on" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                    time.sleep(5)
                    self.off()
                    print("time: %02d:%02d:%02d pump: off" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                break
            except RuntimeError as e:
                print("Pump error:", e.args)
            except KeyboardInterrupt:
                self.off()
                break

    def __del__(self): 
        self.off()
