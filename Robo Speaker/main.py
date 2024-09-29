import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    intro = "Welcome to text to speech RoboSpeaker 1.1 created by Zero"
    print(intro)
    speak(intro)
    outro = "Bye! Have a great day."
    
    while True:
        # Ask the user for input
        text = input("Enter the text you want me to say (Press 'q' to quit): ")

        # Exit if the user enters 'q'
        if text.lower() == "q":
            print(outro)
            speak(outro)
            break

        # Speak the text
        speak(text)

