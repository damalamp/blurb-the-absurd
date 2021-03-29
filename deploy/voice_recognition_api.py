def transcribe_file(recording_path):
    """Transcribe the given audio file."""
    from google.cloud import speech
    import io
    import os
    import sys

    home_path = os.environ['HOME']
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f"{home_path}/google-cloud-api-key.json"

    client = speech.SpeechClient()

    with io.open(recording_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="en-US",
    )

    # Send audio to GCP for transcription.
    response = client.recognize(config=config, audio=audio)

    # Response contains a list of transcription chunks, since the audio recording being transcribed should be short,
    # return just the first result in the response.
    print(f"ZZZ response: {response.results}")
    if len(response.results) == 0:
        print("ERROR: No results returned from transcription. Check if audio file recorded correctly.")
        sys.exit(1)
    top_result = response.results[0].alternatives[0].transcript

    # For longer files, loop over response.results to build the full transcription text.
    ## for result in response.results:
    ##     # The first alternative is the most likely one for this portion.
    ##     print(u"Transcript: {}".format(result.alternatives[0].transcript))

    return top_result
