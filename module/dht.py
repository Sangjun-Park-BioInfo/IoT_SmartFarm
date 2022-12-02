import 


import time
import adafruit_dht
import board
import csv
import spidev as s

#set sensor
dht = adafruit_dht.DHT11(board.D4) #dht
spi = s.SpiDev() #soil moist sensor
spi.open(0, 0)
spi.max_speed_hz = 1000000

def ReadVol(vol):
    adc = spi.xfer2([1, (8 + vol) << 4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

mcp3008 = 0
SLOPE = 2.18
INTERCEPT = -0.79

#set result file
filepath = "./result/"
filename = "result_env_test.csv"
file = open(filepath + filename, 'w', newline = '')
wr = csv.writer(file)
wr.writerow(["time", "temp(*C)", "humidity(%)", "soil moist(%)"])
file.close()


i = 0 #iterator

#measuring every 10 minutes, for a day
while i < (6 * 24):
    try: 
        temp = dht.temperature
        hum = dht.humidity
        
        now = time.localtime()
        current_time = "%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
        
        a_1 = ReadVol(mcp3008)
        Vol = 3.3 * a_1 / 1024 
        moist =  (1.0/Vol) * SLOPE + INTERCEPT
        
        #write result
        file = open(filepath + filename, 'a', newline = '')
        wr = csv.writer(file)
        wr.writerow([current_time, temp, hum, moist])
        file.close()
