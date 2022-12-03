import time
import spi
import RPi.GPIO as GPIO


class pump:

    def __init__(self, moist = 0.14):
        self.status = "off"
        self.moist = moist
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)

    def on(self):
        GPIO.output(17, False)
        self.status = "on"
    def off(self):
        GPIO.output(17, True)
        self.status = "off"

    def test(self):
        print("Pump on")
        self.on()
        time.sleep(5)
        print("Pump off")
        self.off()

    def status(self):
        return self.status

    def operate(self):
        
        while True:
            try:
                spi = spi.spi()    
                moist = spi.measure()
                del spi

                if moist <= self.moist:
                    self.on()
                    time.sleep(5)
                    self.off()
                break
            except RuntimeError as e:
                print("Pump error:", e.args)
            except KeyboardInterrupt:
                self.off()
                break

    def __del__(self): ()