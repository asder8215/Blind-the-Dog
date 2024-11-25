import speech_recognition as sr

class DogCmd():
    GO = 1
    BACKWARD = 2
    LEFT = 3
    RIGHT = 4
    STOP = 0
    WOOF = 6
    WOOFCONFUSED = 7
    ERROR = 8

    def __init__(self):
        self.go_words = {"go", "move", "forward"}
        self.back_words = {"back", "backward", "move back", "come back"}
        self.left_words = {"left", "turn left", "move left"}
        self.right_words = {"right", "turn right", "move right"}
        self.stop_words = {"stop", "pause", "don't move", "stop moving"}
        self.woof_words = {"woof", "bark", "pup"}
        pass
    # Using Google
    def speech_recognition(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                if any(word in text for word in self.go_words):
                    return self.GO
                elif any(word in text for word in self.back_words):
                    return self.BACKWARD
                elif any(word in text for word in self.left_words):
                    return self.LEFT
                elif any(word in text for word in self.right_words):
                    return self.RIGHT
                elif any(word in text for word in self.stop_words):
                    return self.STOP               
                elif any(word in text for word in self.woof_words):
                    return self.WOOF
                else:
                    return self.WOOFCONFUSED
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")
        # for errors
        return self.ERROR

    # Using Sphinx
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

