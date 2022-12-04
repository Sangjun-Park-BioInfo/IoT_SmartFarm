from . import dht
import time
import RPi.GPIO as GPIO

class humidifier:

    def __init__(self, humidity=70):
        self.status = "off"
        self.humidity = humidity
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(23, GPIO.OUT)
        GPIO.output(23, True)

    
    def on(self):
        GPIO.output(23, False)
        self.status = "on"
    def off(self):
        GPIO.output(23, True)
        self.status = "off"

    def test(self):
        print("Humidifier test")
        print("humidifier on")
        self.on()
        time.sleep(10)
        print("humidifier off")
        self.off()
        time.sleep(2)
    
    def stat(self):
        return self.status

    def operate(self):
        i = 0

        while i < 6:
            try:    
                dht = dht.dht()
                data = dht.measure()
                del dht

                if data[1] <= self.humidity:
                    self.on()
                    self.status = "on"
                else:
                    self.off()
                    self.status = "off"
                    i += 1
                time.sleep(599)
            except RuntimeError as e:
                print("Humidifier error:", e.args)
            except KeyboardInterrupt:
                self.off()
                break
    
    def __del__(self): 
        self.off()
