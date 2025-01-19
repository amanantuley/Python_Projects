import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Speak the given text using TTS."""
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    print("Jarvis is ready. Say 'Jarvis' to wake me up.")

# Continuous listening loop
while True:
    try:
        with sr.Microphone() as source:
            # Adjust for ambient noise and listen
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = recognizer.listen(source)  # Record audio input

        # Recognize speech using Google Web Speech API
        try:
            command = recognizer.recognize_google(audio)  # Process recorded audio
            print(f"You said: {command}")

            # Wake word detection
            if "jarvis" in command.lower():
                speak("Yes, I am listening.")
                print("Jarvis is active.")
                
                # Add functionality here, e.g., open a website
                speak("What would you like me to do?")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)
                    task = recognizer.recognize_google(audio).lower()

                    if "open google" in task:
                        speak("Opening Google.")
                        webbrowser.open("https://www.google.com")
                    elif "open youtube" in task:
                        speak("Opening Youtube.")
                        webbrowser.open("https://www.youtube.com/")
                    elif "exit" in task or "quit" in task:
                        speak("Goodbye!")
                        break
                    else:
                        speak("I didn't understand that.")
        
        except sr.UnknownValueError:
            print("I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the Google Speech Recognition service: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
