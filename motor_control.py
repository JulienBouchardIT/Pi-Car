import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25
pause = 1
duty = 100  # Duty cycle, see: https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/
pause_demo = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)
p.start(duty)
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


def exit():
    GPIO.cleanup()


def demo():
    print('Starting demo')
    sleep(pause_demo)
    print('Forward')
    forward()
    sleep(pause_demo)
    print('Backward')
    sleep(pause_demo)
    print('Stop')
    stop()
    exit()


if __name__ == '__main__':
    '''Use for testing only!'''
    demo()

