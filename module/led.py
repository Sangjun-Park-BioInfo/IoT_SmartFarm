import time
import RPi.GPIO as GPIO

class led:
    def __init__(self):
        self.status = "off"

    def GPIOset(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(27, GPIO.OUT)
        GPIO.output(27, True)

    def on(self):
        GPIO.output(27, False)
    def off(self):
        GPIO.output(27, True)

    
    def test(self):
        self.GPIOset()
        while True:
            try:
                self.on()
                time.sleep(2)
                self.off()
                time.sleep(2)
            except RuntimeError as e:
                print("RuntimeError: ", e.args)
            except KeyboardInterrupt:
                self.off()
                break
    
    def status(self):
        return self.status


    def operate(self, start=8, end=19):
        
        self.GPIOset()
        self.timeset(start, end)

        while True:
            try:
                now = time.localtime()
                hour = int(now.tm_hour)

                if hour >= start and hour < end:
                    print("time: %02d:%02d:%02d led: on" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                    self.on()
                    self.status = "on"

                else:
                    print("time: %02d:%02d:%02d led: off" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                    self.off()
                    self.status = "off"
                break
            
            except RuntimeError as e:
                print("RuntimeError: ", e.args)
            except KeyboardInterrupt:
                GPIO.output(27, True)
                break
