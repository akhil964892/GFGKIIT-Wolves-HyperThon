from flask import Flask, request, jsonify
import pyttsx3
import webbrowser
import wikipedia
import datetime

app = Flask(__name__)

engine = pyttsx3.init()
engine.setProperty('voice', pyttsx3.init('sapi5').getProperty('voices')[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route("/")
def home():
    return "Voice Assistant Backend Running"

@app.route("/process", methods=["POST"])
def process_command():
    data = request.get_json()
    command = data.get("command", "").lower()
    response = ""

    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        response = f"According to Wikipedia: {results}"
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}"
        speak(response)
    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube..."
    elif "shutdown" in command:
        response = "Shutting down system..."
        # Uncomment this if you want to actually shut down the system
        # os.system("shutdown /s /t 1")
    else:
        response = "Sorry, I didn't understand that command."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
