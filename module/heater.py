from . import dht
import time
import RPi.GPIO as GPIO

class heater:

    def __init__(self, temperature=17):
        self.status = "off"
        self.temperature = temperature
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, True)

    
    def on(self):
        GPIO.output(22, False)
        self.status = "on"
    def off(self):
        GPIO.output(22, True)
        self.status = "off"

    def test(self):
        print("Heater on")
        self.on()
        time.sleep(120)
        print("Heater off")
        self.off()
    
    def stat(self):
        return self.status

    def operate(self):
        i = 0

        while i < 6:
            try:    
                dht = dht.dht()
                data = dht.measure()
                del dht

                if data[0] <= self.temperature:
                    self.on()
                    self.status = "on"
                else:
                    self.off()
                    self.status = "off"
                    i += 1
                time.sleep(599)
            except RuntimeError as e:
                print("Heater error:", e.args)
            except KeyboardInterrupt:
                self.off()
                break
    
    def __del__(self): 
        self.off()

