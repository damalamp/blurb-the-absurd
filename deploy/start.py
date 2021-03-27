# import blurb_recorder as recorder
# from voice_recognition_api import transcribe_file
# from twitter_api import tweeter
#
# print('Recording Starting...')
# recording_path = recorder.record_for_seconds(10)
#
# print('Sending file for transcription...')
# transcription = transcribe_file(recording_path)
#
# print(f"Transcription result: {transcription}")
#
# print('Sending transcription to be tweeted')
# tweeter(transcription)

import RPi.GPIO as GPIO
import time

red_led_pin = 11
green_led_pin = 13
button_pin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
count = 0

while count < 1000:
    buttonState = GPIO.input(button_pin)
    if buttonState:
      GPIO.output(red_led_pin, GPIO.HIGH)
    else:
      GPIO.output(red_led_pin, GPIO.LOW)
    time.sleep(.1)
    count += 1


# sleep_time = 1
# while count < 3:
#     print(f"count={count}")
#     GPIO.output(green_led_pin, GPIO.LOW)
#     GPIO.output(red_led_pin, GPIO.LOW)
#     time.sleep(sleep_time)
#     GPIO.output(green_led_pin, GPIO.HIGH)
#     GPIO.output(red_led_pin, GPIO.HIGH)
#     time.sleep(sleep_time)
#     count += 1

GPIO.cleanup()
