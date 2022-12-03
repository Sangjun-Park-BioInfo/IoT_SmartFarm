import dht
import time

class heater:

    def __init__(self):
        self.status = "off"
        self.temperature

        GPIO.output(27, False)
    def off(self):
        GPIO.output(27, True)

    def test(self):
        print("Heater on")
        self.on()
        self.status = "on"
        time.sleep(120)
        print("Heater off")
        self.off()
        self.status = "off"
    
    def status(self):
        return self.status

    def operate(self):
        dht = dht.dht()
        data = dht.measure()
        del dht

        if data[0] <= self.temperature:
            self.on()
            self.status = "on"
        else:
            self.off()
            self.status = "off"
        time.sleep(600)