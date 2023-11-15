import pigpio
from time import sleep

GPIO_PIN_1 = 12
GPIO_PIN_2 = 13
GPIO_PIN_3 = 16
GPIO_PIN_4 = 20
GPIO_PIN_5 = 21
GPIO_PIN_6 = 22
GPIO_PIN_7 = 23
GPIO_PIN_8 = 24
GPIO_PIN_9 = 25

pi = pigpio.pi()
pi.set_mode(GPIO_PIN_1, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_2, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_3, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_4, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_5, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_6, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_7, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_8, pigpio.OUTPUT)
pi.set_mode(GPIO_PIN_9, pigpio.OUTPUT)

while True:
    pi.write(GPIO_PIN_9, 1)  # Turn led ON
    sleep(1)
    pi.write(GPIO_PIN_9, 0)  # Turn led OFF
    sleep(1)
    pi.write(GPIO_PIN_9, 1)  # Turn led ON
    sleep(1)
    pi.write(GPIO_PIN_9, 0)  # Turn led OFF
    sleep(1)
    pi.write(GPIO_PIN_2, 1)  # Turn led ON
    sleep(1)
    pi.write(GPIO_PIN_2, 0)  # Turn led OFF
    sleep(1)