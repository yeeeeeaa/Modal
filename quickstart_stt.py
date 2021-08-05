import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=\
                                               "gongmojun1-dd9099481c25.json"

def run_quickstart():
    import io
    import os

    from google.cloud import speech

    client=speech.SpeechClient()

    file_name=os.path.join(os.path.dirname(__file__),".","output.wav")

    with io.open(file_name,"rb") as audio_file:
        content=audio_file.read()
        audio=speech.RecognitionAudio(content=content)

        config=speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="ko-KR",
            )

        response=client.recognize(config=config, audio=audio)

        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))

if __name__=="__main__":
    run_quickstart()
    os.system("touch textfile1")
    os.system("sudo python quickstart_stt.py>textfile1")
