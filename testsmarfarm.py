import smartfarm
from module import led
from module import heater
from module import humidifier
from module import pump
from module import dht
from module import spi
import time

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

    dht = dht.dht()
    print(dht.measure())
    #del dht
    time.sleep(2)

    print("====================")
    print("spi sensor test")
    
    spi = spi.spi()
    print(spi.measure())
    del spi
    
    del smartfarm
