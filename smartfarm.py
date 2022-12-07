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
from module import spi
import adafruit_dht
import board

class smartfarm:

    def time(self):
        return time.localtime()

    def measure(self):
        while True:
            try: 
                temp = dht.temperature
                hum = dht.humidity
                break
            except RuntimeError as e:
                print("dht error:", e.args)
                time.sleep(2)
            except KeyboardInterrupt:
                break
            except OverflowError:
                print("dht overflowerrot")
        
        return (temp, hum)


    def __init__(self, daytime=10, start=8, temp=16, hum=60, moist=0.20,
        filepath="./SmartFarm_result/", filename="smartfarm_log.csv"):
        
        self.day = daytime
        self.start = start
        self.temp = temp
        self.hum = hum
        self.moist = moist

        self.filepath = filepath
        now = time.localtime()
        self.date = "%02d.%02d.%02d_" % (now.tm_year, now.tm_mon, now.tm_mday)
        self.filename = self.date + filename

        self.led = led.led()
        self.heater = heater.heater(self.temp)
        self.humidifier = humidifier.humidifier(self.hum)
        self.pump = pump.pump(self.moist)
        self.spi = spi.spi()


    def timeset(self):
        while True:
            try:
                now = time.localtime()
                min = int(now.tm_min)
                
                if min % 10  == 0:
                    break
                elif min % 10 < 2:
                    time.sleep(360)
                    print("time: %02d:%02d:%02d" % (now.tm_hour, now.tm_min,
                        now.tm_sec), self.measure())
                elif min % 10 < 8:
                    time.sleep(60)
                    print("time: %02d:%02d:%02d" % (now.tm_hour, now.tm_min,
                        now.tm_sec), self.measure())
                else:
                    time.sleep(0.1)

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

        file = open(self.filepath + "pump_log.txt", 'w')
        file.write(self.date + '\n')
        file.close()

    def log(self):
        #time
        now = self.time()
        now_time  = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
        
        #dht
        dht_data = self.measure()

        file = open(self.filepath + self.filename, 'a', newline = '')
        wr = csv.writer(file)
        wr.writerow([now_time, self.led.stat(), self.heater.stat(), 
            self.humidifier.stat(), self.pump.stat(), dht_data[0],
            dht_data[1], self.spi.measure()]) 
        file.close()
    
    
    def operate(self):
        dht_data = self.measure()
        self.led.operate(self.start, self.start + self.day)
        self.heater.operate(dht_data[0])
        self.humidifier.operate(dht_data[1])
        self.pump.operate()
        
    def smartfarm(self):   
        self.operate()
        
        now = self.time()
        if now.tm_min % 10  < 1:
            time.sleep(60)

        self.timeset()

        while True:
            try:
                self.operate()
                self.log()
                time.sleep(60)
                self.timeset()
                
            except RuntimeError as e:
                print("smartfarm.py runtimeerror:", e.args)
            except KeyboardInterrupt:
                break

    def __del__(self): 
        del self.led
        del self.heater
        del self.humidifier
        del self.pump

if __name__ == "__main__":
    dht = adafruit_dht.DHT11(board.D4)
    smartfarm = smartfarm()
    smartfarm.makelog()
    smartfarm.smartfarm()
    del smartfarm



