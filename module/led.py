import time
import RPi.GPIO as GPIO

class led:

    def GPIOset(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(27, GPIO.OUT)
        GPIO.output(27, True)

    def on(self):
        GPIO.output(27, False)

    def off(self):
        GPIO.output(27, True)

    def timeset(self, start, end):
        while True:
            try:
                now = time.localtime()
                min = int(now.tm_min)
                if int(now.tm_hour) >= start  and int(now.tm_hour) < end:
                    self.on()
                else:
                    self.off()

                if min  == 0:
                    break
                elif min < 30:
                    time.sleep(1799)
                elif min < 45:
                    time.sleep(899)
                elif min < 55:
                    time.sleep(179)
                else:
                    time.sleep(5)

            except RuntimeError as e:
                print("RuntimeError: ", e.args)
            except KeyboardInterrupt:
                GPIO.output(27, True)
                break

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
                    time.sleep(3599.9)

                else:
                    print("time: %02d:%02d:%02d led: off" % (now.tm_hour,
                        now.tm_min, now.tm_sec))
                    self.off()
                    time.sleep(3599.9)
            
            except RuntimeError as e:
                print("RuntimeError: ", e.args)
            except KeyboardInterrupt:
                GPIO.output(27, True)
                break
