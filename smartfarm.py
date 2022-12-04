#This code is the main code operating smarfarm system including led, heater, hu
#midifier, water pump using the data from dht sensor, spi(soil moist) sensor. 
#Maintainer: Sangjun Park

#Information about devices and sensors
#led is controlled by GPIO 27 via relay, and it needs 12V DC power
#heater is controlled by GPIO 22 via relay, and it needs 12V DC power
#humidifier is controlled by GPIO 23 via relay, and it needs 5V DC power
#water pump is controlled by GPIO 17 via relay, and it needs 5V DC power

#data from dht sensor is received via GPIO 4, and this sensor needs 3.3V DC pow
#er
#data fromm spi sensor is received via mcp3008chip-GPIO 8, 9, 10, 11 connection
#, and this sensor needs 3.3V DC power 

import time
import csv
from module import led
from module import heater
from module import humidifier
from module import pump
from module import dht
from module import spi


class smartfarm:

    def __init__(self, daytime=10, start=8, temp=16, hum=60, moist=0.14,
        filepath="./Smartfarm_result", filename="smartfarm_result.csv"):
        
        self.day = daytime
        self.start = start
        self.temp = temp
        self.hum = hum
        self.moist = moist

        self.filepath = filepath
        now = time.localtime()
        date = "%02d.%02d.%02d_" % (now.tm_year, now.tm_mon, now.tm_mday)
        self.filename = date + filename

        led = led.led()
        heater = heater.heater(self.temp)
        humidifier = humidifier.humidifier(self.hum)
        pump = pump.pump(self.moist)

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
        wr.writerow(["Time", "led","Heater",  "Humidifier", "Pump",
            "Temperature(*C)", "Humidity(%)", "Soil moisture"])
        file.close()

    def log(self):
        #time
        now = time.localtime()
        time = "%02d.%02d.%02d_" % (now.tm_hour, now.tm_min, now.tm_sec)
        
        #temperature, humidity
        dht = dht.dht()
        temp = dht.measure()[0]
        hum = dht.measure()[1]
        del dht
        #soil moist
        spi = spi.spi()
        moist = spi.measure()
        del soil

        file = open(self.filepath + self.filename, 'w', newline = '')
        wr = csv.writer(file)
        wr.writerow([time, led.status(), heater.status(), humidifier.status(),
            pump.status(), temp, hum, soil, moist]) 
        file.close()
    
    
    def operate(self):
        led.operate(self.start, self.start + self.day)
        heater.operate(self.temp)
        humidifier.operate(self.hum)
        pump.operate(self.moist)
        
    def smartfarm(self):   
        self.operate()
        self.timeset()

        while True:
            try:
                self.log()
                self.operate()
                time.sleep(3550)
                self.timeset()
                
            except RuntimeError as e:
                print("smartfarm.py runtimeerror:", e.args)
            except KeyboardInterrupt:
                break

    def __del__(self):
        del led
        del heater
        del humidifier
        del pump

if __name__ == "__main__":
    smartfarm = smartfarm()
    smartfarm.makelog()
    smartfarm.smartfarm()
    del smartfarm



