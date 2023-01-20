import pyttsx3
  
engine = pyttsx3.init()

# voices = engine.getProperty('voices')
  
# for voice in voices:
#     # to get the info. about various voices in our PC 
#     print("Voice:")
#     print("ID: %s" %voice.id)
#     print("Name: %s" %voice.name)
#     print("Age: %s" %voice.age)
#     print("Gender: %s" %voice.gender)
#     print("Languages Known: %s" %voice.languages)

# For Zira, Voice ID:
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
  
# Use female voice
engine.setProperty('voice', voice_id)

# Set rate
# engine.setProperty('rate', 90)
# Set volume 0-1
# engine.setProperty('volume', 0.9)

# file = open("text.txt", "w")
# file.write("Bye Bye")
# print(file) 
# engine.say(file)

engine.say("Namashkaar")

engine.runAndWait()