import smartfarm
from module import led
from module import heater
from module import humidifier
from module import pump
import adafruit_dht
import board
from module import spi
import time
import RPi.GPIO as GPIO

'''GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)'''
dht = adafruit_dht.DHT11(board.D4)

def measure():
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
    
    return (temp, hum)


if __name__ == "__main__":
    
    smartfarm = smartfarm.smartfarm()
    smartfarm.makelog()
    smartfarm.log()
    
    led = led.led()
    led.test()
    del led
    
    print("====================")
    
    heater = heater.heater()
    heater.test()
    del heater

    print("====================")

    humidifier = humidifier.humidifier()
    humidifier.test()
    del humidifier

    print("====================")
    
    pump = pump.pump()
    pump.test()
    del pump

    print("====================")
    print("dht sensor test")
    dht_data = dht.measure()
    print("Temp: %2d*C Humid: %2d%" % (dht_data[0], dht_data[1]))
    
    time.sleep(2)

    print("====================")
    print("spi sensor test")
    
    spi = spi.spi()
    print(spi.measure())
    del spi
    
    del smartfarm
