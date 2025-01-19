import time
import pyautogui
import pyperclip
import pyttsx3
import webbrowser

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the text using text-to-speech."""
    engine.say(text)
    engine.runAndWait()

def send_reply(message):
    """Send an automated reply based on the incoming message."""
    responses = {
        "hello": "Hi there! How can I assist you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "bye": "Goodbye! Have a wonderful day!",
    }

    default_reply = "I'm sorry, I didn't quite catch that. Can you rephrase?"
    reply = responses.get(message.lower(), default_reply)

    pyperclip.copy(reply)  # Copy the reply to the clipboard
    pyautogui.hotkey("ctrl", "v")  # Paste the reply
    pyautogui.press("enter")  # Send the message
    speak(reply)  # Speak the reply for added interactivity

def read_message():
    """Read the latest message on WhatsApp."""
    pyautogui.click(x=300, y=900)  # Adjust coordinates to your setup
    time.sleep(1)

    # Simulate triple-click to select message text
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

    pyautogui.hotkey("ctrl", "c")  # Copy selected text
    return pyperclip.paste()  # Retrieve copied text

if __name__ == "__main__":
    speak("Opening WhatsApp Web...")
    print("Opening WhatsApp Web...")
    
    # Open WhatsApp Web in the default browser
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(15)  # Wait for WhatsApp Web to load. Adjust if necessary.

    speak("WhatsApp AutoReply Bot is now active!")
    print("WhatsApp AutoReply Bot is now running. Ensure WhatsApp Web is open and visible.")

    while True:
        try:
            # Read the latest message
            incoming_message = read_message()
            print(f"Received: {incoming_message}")

            # Send an appropriate reply
            send_reply(incoming_message)

            # Wait before checking for new messages
            time.sleep(5)  # Adjust delay as needed
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)  # Retry after a short delay
