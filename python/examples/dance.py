from servosix import ServoSix
import time

ss = ServoSix()

dance = [     
  #lh  lf  rf  rh
  [90, 90, 90, 90],
  [130, 30, 30, 130],
  [30, 130, 130, 30]    
]

delay = 0.2 
 
  
def dance_step(step): 
  ss.set_servo(1, step[0])
  ss.set_servo(2, step[1])
  ss.set_servo(3, step[2])
  ss.set_servo(4, step[3])
  


while (True): 
  for step in dance:
      dance_step(step)
      time.sleep(delay)