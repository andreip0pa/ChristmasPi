from sense_hat import SenseHat
import random
import time
sense = SenseHat()

print sense.get_temperature()


def fill(r,g,b):
  i=0
  j=0
  while i<8:
    j=0
    while j<8:
      sense.set_pixel(i,j,r,g,b)
     # print(i,j)
      j=j+1
      
    i=i+1
    

def isnotfull():
   i=0
   j=0
   while i<8:
    j=0
    while j<8:
      if sense.get_pixel(i,j)==[0,0,0]:
        return 1
     # print(i,j)
      j=j+1
      
    i=i+1
   return 0
   


while (1==1):
  
  temp=sense.get_temperature()
  if (temp>0 and temp<25):
    fill(0,(temp*10)%255,0)
  else:
    if (temp>25):
      fill((temp*10)%255,0,0)
    else:
      fill(0,0,((-temp)*10)%255)
  
  