from RPi import GPIO
from time import sleep
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

shutter_closed = 1
shutter_opened = 0

shutter_value = input("Shutter value: ")
print("Ref. \t Measure. \t Diff. %")

shutter_value_microsec = int(eval(str(shutter_value)) * 1000000)

while(True):
  current_state = GPIO.input(17)
  if(current_state == shutter_opened):
    t1 = datetime.now()

    while(current_state == shutter_opened):
      current_state = GPIO.input(17)

    microsec = (datetime.now() - t1).microseconds
    difference_micro = shutter_value_microsec - microsec
    difference = difference_micro / (shutter_value_microsec * 0.01)
    print(shutter_value_microsec,"\t", microsec, "\t ", str(round(difference, 1)) + "%")

GPIO.cleanup()
