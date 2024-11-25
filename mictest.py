from mic_recognition import DogCmd

def main():
    dog_test = DogCmd()

    result = dog_test.speech_recognition()
    print("Recognition result:", result)

if __name__ == "__main__":
    main()