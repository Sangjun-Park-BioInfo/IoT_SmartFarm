import time
import RPi.GPIO as GPIO

class led:
    def __init__(self):
        self.status = "off"  
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(27, GPIO.OUT)
        GPIO.output(27, True)

    def on(self):
        GPIO.output(27, False)
        self.status = "on"

    def off(self):
        GPIO.output(27, True)
        self.status = "off"
    
    def test(self):
        print("Led test")
        i = 0
        while i < 2:
            try:
                self.on()
                print("led on")
                time.sleep(1)
                self.off()
                print("led off")
                time.sleep(1)
                i += 1
            except RuntimeError as e:
                print("RuntimeError: ", e.args)
            except KeyboardInterrupt:
                self.off()
                break
    
    def stat(self):
        return self.status


    def operate(self, start=8, end=19):

        while True:
            try:
                now = time.localtime()
                hour = int(now.tm_hour)

                if hour >= start and hour < end:
                    print("time: %02d:%02d:%02d led: on" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                    self.on()

                else:
                    print("time: %02d:%02d:%02d led: off" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                    self.off()
                break
            
            except RuntimeError as e:
                print("Led error:", e.args)
            except KeyboardInterrupt:
                self.off()
                break

    def __del__(self): 
        self.off()
