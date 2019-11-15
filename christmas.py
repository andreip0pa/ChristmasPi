from sense_hat import SenseHat
import random
import time
sense = SenseHat()

while 1==1:
  
  timecounter=0.5
  patternchoose=random.randint(1,10)
  i=0
  j=0
  
  while i<8:
    
    j=0
    while j<8:
      time.sleep(timecounter)
      if patternchoose==1:
        sense.set_pixel((i+j)%8,j, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==2:
        sense.set_pixel((i*j)%8,j, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==3:
        sense.set_pixel((i-j)%8,j, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==4:
        sense.set_pixel(j,i, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==5:
        sense.set_pixel(i,j, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==6:
        sense.set_pixel((i*j)%8,(i-j)%8, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==7:
        sense.set_pixel((i-j)%8,(j*j)%8, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==8:
        sense.set_pixel((i*i)%8,(j+(i+1))%8, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==9:
        sense.set_pixel((i%(j+1))%8,(j*2)%8, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      if patternchoose==10:
        sense.set_pixel(i%8,-j%8, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
      
      
      
      j=j+1
      
      
    i=i+1
    
    
  i=0
  j=0
  c=random.randint(1,8)
  while i<8:
    
    j=0
    while j<8:
      time.sleep(0.0001)
      sense.set_pixel(i,j%8,0,0,0)
      
      
      j=j+c
    i=i+1 
    
  i=0
  j=0
  c=random.randint(1,8)
  while i<8:
    
    j=0
    while j<8:
      time.sleep(0.0001)
      sense.set_pixel((i+j)%8,j%8,0,0,0)
      
      
      j=j+1
    i=i+1 
  