import speech_recognition as sr

# Using Google
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    try:
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")


# # Using Sphinx
# recognizer = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = recognizer.listen(source)
# try:
#     text = recognizer.recognize_sphinx(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Sorry, I couldn't understand the audio.")
# except sr.RequestError as e:
#     print(f"Sphinx error: {e}")
