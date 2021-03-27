import blurb_recorder as recorder
from voice_recognition_api import transcribe_file
from twitter_api import tweeter

print('Recording Starting...')
recording_path = recorder.record_for_seconds(10)

print('Sending file for transcription...')
transcription = transcribe_file(recording_path)

print(f"Transcription result: {transcription}")

print('Sending transcription to be tweeted')
tweeter(transcription)
