# GFGKIIT-Wolves-HyperThon
KIIT GFG HYPERTHON
## Bunty: Your AI Personal Assistant

## Overview
Bunty is a voice-controlled AI assistant designed to make your daily tasks easier and more efficient. It can interact with users, perform searches, manage tasks, open applications, and even crack jokes to brighten your day. Built with Python, it integrates various libraries to provide a seamless and interactive user experience.

--- 

## Features
1. Search Capabilities:
   - Retrieve concise summaries from *Wikipedia*.
   - Perform **Google searches** for any query.

2. Greetings & Conversations:
   - Greet users based on the time of the day.
   - Respond to casual questions and fun queries.

3. Social Media Integration:
   - Open **Facebook**, **Instagram**, **Twitter**, **YouTube**, and more.
   - Navigate to specific sections like YouTube Trending or Facebook Friend Requests.

4. Utilities:
   - Send emails (pre-configured with a Gmail account).
   - Open specific files, folders, or applications like Telegram, Discord, or Reddit.
   - Capture photos using the system's camera.
   - Set reminders using desktop notifications.
   - Retrieve the current date and time.

5. Entertainment:
   - Play YouTube videos, trending shorts, and music.
   - Chat about favorite superheroes, movies, and hobbies.

6. System Commands:
   - Shut down your computer.
   - Open system applications like Chrome and File Explorer.

---

## Prerequisites
To run Bunty, you will need:
1. Python 3.7 or higher.
2. Install the required Python libraries:
   ```bash
   pip install pyttsx3 wikipedia speechrecognition ecapture pywhatkit pyautogui win10toast requests bs4
   ```

---

## **How to Run**
1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the program:
   ```bash
   python bunty_assistant.py
   ```
5. Speak into the microphone to interact with Bunty. Use commands like:
   - "Wikipedia Elon Musk."
   - "Open YouTube trending page."
   - "What is the time?"
   - "Set a reminder."
   - "Send mail to Akhil Singh."
   - "Shutdown."

---

## Code Highlights
- Voice Recognition: Captures and processes user speech using `speechrecognition`.
- Text-to-Speech: Converts text to voice with `pyttsx3`.
- Web Automation: Opens and interacts with websites using `webbrowser`.
- Email Integration: Sends emails using Gmail's SMTP server.
- Error Handling: Includes graceful handling of unrecognized commands.

---

## Example Queries
### Input:
1. "Wikipedia Python programming language."
2. "Open Facebook."
3. "Shutdown."
4. "Set a reminder."

### Output:
1. "According to Wikipedia: Python is a high-level, general-purpose programming language..."
2. Facebook's homepage opens in your default browser.
3. System shuts down in 5 seconds.
4. Notification appears after the specified time.

---

## Customization
You can customize the following:
- Social Media URLs: Update the URLs in the script to suit your preferred social media sites.
- File Paths: Modify file paths to point to your system's directories or applications.

---

## Contributors
- Akhil Singh
  - KIIT University
  - Coding and Financial Enthusiast
- Rishi Raj Verma
  - KIIT University 

---

## Acknowledgments
This project was developed as part of the Hyperthon event hosted by GFG KIIT.

---

## **Disclaimer**
This application is for personal use and educational purposes only. Make sure to keep your email credentials secure and avoid sharing them in the code.

---

Let me know if you need any changes or enhancements!
