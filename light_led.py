import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

def off():
 GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
 GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
 GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

def on():
 GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
 GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
 GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)

def red():
 off()
 GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)

def green():
 off()
 GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)

def blue():
 off()
 GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)




# STD command:


def up(power):
    if power:
        GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
    else:
        GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)


def down(power):
    # todo: implement
    print("")


def right(power):
    if power:
        GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
    else:
        GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)


def left(power):
    if power:
        GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH)
    else:
        GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
