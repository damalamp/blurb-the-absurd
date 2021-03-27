import blurb_recorder as recorder
import voice_recognition_api as transcriber

print('Recording Starting...')
recording_path = recorder.record_for_seconds(10)

print('Sending file for transcription...')
transcription = transcriber.transcribe_file(recording_path)

print(f"Transcription result: {transcription}")

# Next: Send transcription text to be tweeted...