import blurb_recorder as recorder
import voice_recognition_api as transcriber

print('ZZZ This is the start.py file running on the raspberry pi')

recording_path = recorder.record_for_seconds(10)
response_dict = transcriber.transcribe_file(recording_path)
