import time
import adafruit_dht
import board
#import heater
#import humidifier

class dht:
    def __init__(self):
        self.dht = adafruit_dht.DHT11(board.D4) #dht      
    
    def measure(self):
        while True:
            try: 
                temp = self.dht.temperature
                hum = self.dht.humidity
                break
            except RuntimeError as e:
                continue
            except KeyboardInterrupt:
                break
        
        return (temp, hum)

    
    def __del__(self): ()