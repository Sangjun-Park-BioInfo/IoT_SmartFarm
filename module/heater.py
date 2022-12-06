import time
import RPi.GPIO as GPIO

class heater:

    def __init__(self, temperature=17):
        self.status = "off"
        self.target = temperature
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
        print("Heater test")
        print("Heater on")
        self.on()
        time.sleep(10)
        print("Heater off")
        self.off()
        time.sleep(2)

    def stat(self):
        return self.status

    def operate(self, current_temp):
        while True:        
            try:    
                now = time.localtime()
                
                if current_temp <= self.target:
                    self.on()
                    print("time: %02d:%02d:%02d heater: on" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                else:
                    self.off()
                    print("time: %02d:%02d:%02d heater: off" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                break
            except RuntimeError as e:
                print("Heater error:", e.args)
            except KeyboardInterrupt:
                self.off()
                break
    
    def __del__(self): 
        self.off()

