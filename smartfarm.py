import time
import csv
from module import led
from module import dht
from module import heater
'''import heat
import hum
import led
import cam'''


led = led.led()
heater = heater.heater()

class smartfarm:

    def __init__(self, day=10, start=8, filepath="./Smartfarm_result", 
        filename="smartfarm_result.csv"):
        self.day = day
        self.start = start
        self.filepath = filepath
        now = time.localtime()
        date = "%02d.%02d.%02d_" % (now.tm_year, now.tm_mon, now.tm_mday)
        self.filename = date + filename
        

        '''self.dht = dht
        self.spi = spi
        self.heat = heat
        self.hum = hum
        self.led = led
        self.cam = cam'''

    def timeset(self):
        while True:
            try:
                now = time.localtime()
                min = int(now.tm_min)
                
                if min  == 0:
                    break
                elif min < 30:
                    time.sleep(1799)
                elif min < 45:
                    time.sleep(899)
                elif min < 59:
                    time.sleep(59)
                else:
                    time.sleep(0.01)

            except RuntimeError as e:
                print("RuntimeError from smartfarm.py: ", e.args)
            except KeyboardInterrupt:
                break

    def makelog(self): #CSV result file 생성
        
        file = open(self.filepath + self.filename, 'w', newline = '')
        wr = csv.writer(file)
        wr.writerow(["Time", "led" "Temperature(*C)", "Heater", "Humidity(%)",
            "Humidifier", "Soil moisture", "Pump"])
        file.close()

    #led, dht, heater, humidifier, soil sensor, pump 객체로부터 작동 여부를 입력받아 기록
    def log(self, led, temp, heater, hum, humidifier, soil, pump):
        now = time.localtime()
        time = "%02d.%02d.%02d_" % (now.tm_hour, now.tm_min, now.tm_sec)
        
        file = open(self.filepath + self.filename, 'w', newline = '')
        wr = csv.writer(file)
        wr.writerow([time, led.status(), ]) #시간, led점등, 온도, 히터동작, 습도, 가습기, 토양수분, 펌프동작 작성
        file.close()
    
    
    def operate(self):
        led.operate(self.start, self.start + self.day)
        
        #가습기 동작
        #관수펌프 동작



        


if __name__ == "__main__":
    smartfarm = smartfarm()



