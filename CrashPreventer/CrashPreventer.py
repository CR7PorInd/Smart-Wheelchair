#this code should be done in the GPIO library in python(otherwise it done not work
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#VCC - pin 2
#GND to pin 6
#TRIG too pin 12
# connect the 330 ohms resistor to echo . on its end you connect it to pin 18 and through 470 ohms resistor u connect it also to pin 6
GPIO_ECHO=18
GPIO_TRIG=24
GPIO.setup(GPIO_TRIG,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
def distance():
    GPIO.output(GPIO_TRIG,True)
# set trigger after 0.01 min to Low
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG,False)
    StartTime=time.time()
    StopTime=time.time()
    while GPIO.input(GPIO_ECHO)==0:
        StartTime=time.time()
    while GPIO.input(GPIO_ECHO)==1:
        StopTime=time.time()
    TimeElapsed= StopTime - StartTime
    distance =(TimeElapsed * 34300)/2
    return distance

if_name_=='_main_':
    try:
        while True:
            dist=distance()
            print("measured distance = %.1f cm" % dist)
            time sleep(1)
# reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("measurement stopped by user")
        GPIO.cleanup()


    


