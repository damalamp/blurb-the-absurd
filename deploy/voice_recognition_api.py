def transcribe_file(recording_path):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io
    import os

    # print(f"ZZZ os env: {os.environ['GOOGLE_APPLICATION_CREDENTIALS']}")
    home_path = os.environ['HOME']
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{home_path}/google-cloud-api-key.json"
    print('ZZZ Printing env vars:')
    for k, v in os.environ.items():
        print(f'{k}={v}')
    client = speech.SpeechClient()

    with io.open(recording_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
