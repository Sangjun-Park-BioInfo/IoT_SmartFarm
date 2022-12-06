import time
import RPi.GPIO as GPIO

class humidifier:

    def __init__(self, humidity=70):
        self.status = "off"
        self.target = humidity
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

    def operate(self, current_hum):
        while True:
            try:    
                now = time.localtime()
                
                if current_hum <= self.target:
                    self.on()
                    print("time: %02d:%02d:%02d humidifier: on" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                else:
                    self.off()
                    print("time: %02d:%02d:%02d humidifier: off" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                break
            except RuntimeError as e:
                print("Humidifier error:", e.args)
            except KeyboardInterrupt:
                self.off()
                break
    
    def __del__(self): 
        self.off()
