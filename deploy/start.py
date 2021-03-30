import blurb_recorder as recorder
from voice_recognition_api import transcribe_file
from twitter_api import tweeter

import RPi.GPIO as GPIO
import time

red_led_pin = 11
green_led_pin = 13
button_pin = 15


def red_led_on(self):
    print(f"Button press detected")
    GPIO.output(green_led_pin, GPIO.HIGH)
    GPIO.output(red_led_pin, GPIO.LOW)
    print('Recording Starting...')
    recording_path = recorder.record_for_seconds(10)
    GPIO.output(red_led_pin, GPIO.HIGH)
    print('Sending file for transcription...')
    transcription = transcribe_file(recording_path)

    print(f"Transcription result: {transcription}")

    print('Sending transcription to be tweeted')
    tweeter(transcription)
    GPIO.output(red_led_pin, GPIO.LOW)
    time.sleep(.2)
    GPIO.output(red_led_pin, GPIO.HIGH)
    time.sleep(.4)
    GPIO.output(green_led_pin, GPIO.LOW)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.output(red_led_pin, GPIO.HIGH)  # HIGH = off
GPIO.output(green_led_pin, GPIO.LOW)  # LOW = on
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button_pin, GPIO.RISING, callback=red_led_on, bouncetime=12000)
time.sleep(2e6)

GPIO.cleanup()
