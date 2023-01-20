import speech_recognition as sr

# file = "Pasoori - Shae Gill.mp3"

r = sr.Recognizer()

# with sr.AudioFile(file) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    
    # convert speech to text

    text = r.recognize_google(audio_data)
    # text = r.recognize_google(audio_data, language="es-ES")
    print(text)










