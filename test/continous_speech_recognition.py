import speech_recognition as sr
import os
import vosk
import time

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Set vosk model
vosk.Model("model")

# Continious outputing of speech for every 3 second recognition
output = ''
# with sr.Microphone() as source:
#     print("Adjusting for ambient noise...")
#     r.adjust_for_ambient_noise(source,duration=1)
#     r.pause_threshold = 0.1
#     r.non_speaking_duration = 0.1

#     print("Talk")
#     while True:
#         audio = r.listen(source, timeout=1)

#         try:
#             text = r.recognize_vosk(audio, language='en-US')
#             output += text + ' '
#             os.system('cls')
#             print(output)
#         except Exception as e:
#             print(e)
    
#  This is nice, however, lets not wait the speaker to finish the sentence, and abruply stop the recording. We should also not wait for the speaker to start speaking, we will go ahead recognize immediately. This will go on for every 3 seconds.
with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    r.adjust_for_ambient_noise(source,duration=1)
    r.pause_threshold = 0.1
    r.non_speaking_duration = 0.1

    print("Talk")
    while True:
        audio = r.record(source, duration=2)
        t1 = time.time()
        try:
            text = r.recognize_google(audio, language='en-US')
            output += text + ' '
            os.system('cls')
            print(output, time.time()-t1)
        except Exception as e:
            print(e)