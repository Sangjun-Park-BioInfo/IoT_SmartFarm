from . import smartfarm
from module import led
from module import heater
from module import humidifier
from module import pump
from module import dht
from module import spi


if __name__ == "__main__":
    smartfarm = smartfarm()
    smartfarm.makelog()
    smartfarm.log()
    
    led = led.led()
    led.test()
    del led

    heater = heater.heater()
    heater.test()
    del heater

    humidifier = humidifier.humidifier()
    humidifier.test()
    del humidifier

    pump = pump.pump()
    pump.test()
    del pump

    dht = dht.dht()
    print(dht.measure())
    del dht

    spi = spi.spi()
    print(spi.measure())
    del spi

    del smartfarm
