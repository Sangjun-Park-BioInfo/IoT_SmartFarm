import adafruit_dht
import board

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

print("=================\ndht test\n=================")

temp = measure()[0]
hum = measure()[1]
print(temp, hum)
