import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1. created by Namita")
    x = input("Enter what you want me to speak: ")

    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
