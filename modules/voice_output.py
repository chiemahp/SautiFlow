from gtts import gTTS

def generate_speech(text, output_path="response.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)
    return output_path
