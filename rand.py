from sense_hat import SenseHat
import time
import random
sense = SenseHat()


while True:
  acc=sense.get_accelerometer_raw()
  if (abs(acc['x'])>0 and abs(acc['y'])>0 and abs(acc['z'])>1  ):
    print(random.randint(1,6))
    time.sleep(2)