import time
import spidev as s

class spi:

    def __init__(self):
        self.spi = s.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000

    def ReadVol(self, vol):
        adc = self.spi.xfer2([1, (8 + vol) << 4, 0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

    

    def measure(self):
        while True:
            try:
                mcp3008 = 0
                SLOPE = 2.18
                INTERCEPT = -0.79
                
                a_1 = self.ReadVol(mcp3008)
                Vol = 3.3 * a_1 / 1024
                break
            except RuntimeError as e:
                print("soil sensor error:", e.args)
                time.sleep(2)
            except KeyboardInterrupt:
                break
        
        return ((1.0/Vol) * SLOPE) + INTERCEPT

    def __del__(self): ()
        
