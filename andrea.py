from gpiozero import Device, LED                                                  # (1)
from gpiozero.pins.pigpio import PiGPIOFactory                                    # (2)
from time import sleep
import sys
import signal
Device.pin_factory = PiGPIOFactory()


def init_leds(pin_numbers):
    output = []
    for num in pin_numbers:
        output.append(LED(num))
    return output

def all_on(pins):
    for pin in pins:
        pin.on()

def all_off(pins):
    for pin in pins:
        pin.off()

pins=init_leds([12,13,16,20,21,22,23,24,25])

all_on(pins)
sleep(1)
all_off(pins)
sleep(1)

def blink_combo(student_id):
    for num in student_id:
        pins[num-1].on()
        sleep(1)
        pins[num-1].off()
        sleep(1)    

def strobe_reg(pins,time):
    while True:
        all_off(pins)
        sleep(time)
        all_on(pins)
        sleep(time)

def signal_handler(sig, frame):
    all_off(pins)
    sys.exit(0)

# Andrea
blink_combo([9,9,2])

#Rahul
blink_combo([2,7,1])

#Aryan
blink_combo([6,2,5])

strobe_reg(pins,0.5)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler) # Captures when CTRL - c is pressed
