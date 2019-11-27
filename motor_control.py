import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25
pause = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)
p.start(25)  # Duty cycle
p.ChangeDutyCycle(50)  # Speed, should be between 25 et 75 (50 = medium)


def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)


def forward():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)


def backward():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)


def demo():
    print('Starting demo')
    sleep(1)
    print('Forward')
    forward()
    sleep(1)
    print('Backward')
    sleep(1)
    print('Stop')
    stop()


if __name__ == '__main__':
    '''Use for testing only!'''
    demo()

