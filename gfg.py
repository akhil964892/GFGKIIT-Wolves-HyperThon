import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os
import time
from bs4 import BeautifulSoup
import requests
import ecapture as ec
import pywhatkit
import pyautogui
from win10toast import ToastNotifier
import subprocess
pyautogui.alert(''' Our program includes the following functions-
wikipedia
greetings
time
facebook main page
facebook friend request
facebook notifications
youtube main page
youtube trending page
youtube shorts
camera
google search
shutdown
''')



# engine=pyttsx3.init()
engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")

    elif hour>=12 and hour<18 :
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hi this is bunti, how can I help you ?")      

def takeCommand():
    #it takes microphene input from the user and returns string output

    r  = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshhold = 1
        audio =r.listen(source)

    try  :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')    
        print(f"User said:{query}\n")

    except Exception as e :
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('22051570@kiit.ac.in', 'enter password')
    server.sendmail('22051570@kiit.ac.in', to, content)
    server.close()

   
if __name__ == "__main__":
    wishme()
    while True :
     
   
         query = takeCommand().lower()
    #logic  for xecuting tasks
         if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia", "")
            results  = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            continue

         
         elif 'how r u' in query:
            speak('i am good , what about u')
            continue
         elif 'i am fine, can u do something to make me feel alive ' in query:
            webbrowser.open('yes definitely sir, what can i do for u , would u like to listen some music or say something of your choice')
            continue
     
         elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H-%M-%D")
            speak(f"sir the time is {strTime}")
            continue

         elif 'the date' in query :
            strTime = datetime.datetime.now().strftime("%Y-%M-%D")
            speak(f"sir the date is {strTime}")
            continue

         #the function to send emails
         elif 'send mail to akhil singh' in query :
            try:
                speak("what  should i say ")
                content = takeCommand()
                to = "22051570@kiit.ac.in"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e :
                print(e)
                speak("Sorry dear i was not able to send the mail at the")
            continue


          #knowing everything about followers
         elif 'open instagram' in query:
            pyttsx3.speak("what do youu want to do on instagram")
            querye = takeCommand().lower()
            if 'number of followers' in query :
               
                print("...")

            print (".....")
            webbrowser.open("instagram.com")
            continue


            #to do anything on twitter
         elif 'open twitter' in query:
            pyttsx3.speak("opening Twitter ")
            print (".....")
            webbrowser.open("twitter.com")
            continue


            #to do anything on facebook
         elif 'open facebook' in query:
            pyttsx3.speak('where do you want to go in facebook')
            queryc = takeCommand().lower()
            if 'main' in queryc:
                pyttsx3.speak("opening Facebook ")
                print (".....")
                webbrowser.open("facebook.com")
            elif 'open friend requests' in queryc:
                pyttsx3.speak('opening friend request list')
                print(".....")
                webbrowser.open("facebook.com/friends")
            continue    



                #to  do any  thing on youtubee
         elif 'open youtube' in query:
           
            pyttsx3.speak('where do you want to go in youtube')
            queryb = takeCommand().lower()
            if 'main' in query:
                webbrowser.open("youtube.com")            
            elif 'trending page' in queryb:
                pyttsx3.speak('showing trending page')
                print(".....")
                webbrowser.open("youtube.com/feed/trending")
            elif 'shorts' in queryb:
                pyttsx3.speak("showing shorts")
                print(".....")
                webbrowser.open("youtube.com/shorts")
            continue    



                #code for system shutdown
         elif 'shutdown' in query:
            pyttsx3.speak("Shutting down")
            print('shutting down.....')
            time.sleep(5)
            os.system(r"shutdown /s /t 1")
            continue    



            #code to open any file in an system
         elif 'open file' in query :
            file_dir = 'C:\\Users\\Default'
            files =os.listdir(file_dir)
            print(files)
            os.startfile(os.path.join(file_dir, files[1]))
         elif 'instagram followers' in query:
           file_dir = 'C:\\Users\\KIIT\\Desktop\\java files'
           files = os.listdir(file_dir)
           print(files)
           os.startfile(os.path.join(file_dir, files[7]))  


           continue  

         
         
          #to search anything on google
         elif 'google search' in query or 'search' in query or 'google' in query:  

                 
            pyttsx3.speak("say what you want to search in google")
            print("say what you want to search in google")
            queryd = takeCommand().lower()
            x=queryd.split()
            print (x)
            y=""
            for i in range (len(x)):
               if i<(len(x)-1):
                    y+=x[i]
                    y+=(r"+")
               else:
                    y+=x[i]
            z=r"google.com/search?q="
            z+=y
            pyttsx3.speak("Searching")
            print("Searching......")
            webbrowser.open(z)
            continue


            #to capture images
         elif 'camera' in query:
            ec.capture(0,'camera','im1.jpg')
            continue
         
         


                #to set a reminder
         elif 'set a reminder' in query :
            speak("setting....")
            toaster = ToastNotifier()

            Toasttitle = input("\nTitle of Remainder: ")
            msg = input("Message: ")
            minutes = float(input("How many Minutes: "))
            seconds = minutes * 60
            print("\nRemainder Set Successfully!\n")
            time.sleep(seconds)
            toaster.show_toast(Toasttitle, msg, duration=10, threaded=True)

            while toaster.notification_active:
                time.sleep
            continue        


                #to do some other ordinary things qith the bunty
         
         elif 'How r u' in query:
            speak("I am fine. What about you")
            continue
         elif 'who created you' in query:
            speak("WOLVES: AKHIL SINGH AND RISHI RAJ VERMA")
            continue
         elif 'when you were born' in query:
            speak("I am still in progress, I havent taken birth properly")
            continue
         elif 'Bunty tera sabun slow hai kya' in query:
            speak("mera nahi par tumhara hoga")
            continue
         elif 'where you were born' in query:
            speak("In School of computer engineering campus")  
            continue
         elif 'what do you like to do' in query:
            speak("Serving my master is the most enjoyable thing for me")
            continue
       
         
         
         elif 'good morning bunty' in query :
            speak("good morning, master have a beautifu day ahead")
            continue
         elif 'good afternoon bunti' in query :
            speak("good afternoon, master")  
            continue
         elif 'good evening bunti' in query :
            speak("good evening, master")  
            continue
         elif 'good night bunty' in query :
            speak("good night, master")
            continue  
         elif 'who is your favourite superhero' in query :
            speak("Iron man, love you 3000")
            continue
         
   
         elif 'which is your favourite movie' in query :
            speak("I don't watch movies very often but Interstellar is my favourite")
            continue
         elif 'open chrome' in query :
            pyttsx3.speak("opening chrome")
            print(".")
            print(".")
            os.system("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
            continue
         elif 'open telegram' in query: 
            pyttsx3.speak("Opening Telegram") 
            print(".") 
            print(".") 
            telegram_path = "C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_5.10.3.0_x64__t4vj0pshhgkwm\\Telegram.exe" 
            try: subprocess.Popen(telegram_path, shell=True) 
            except PermissionError: print("Access is denied. Please try running your script as an administrator.") 
            except Exception as e: print(f"An error occurred: {e}") 
            continue
            #######
         elif 'open file explorer' in query:
            file_dr= 'C:\\Users\\KIIT\\Documents'
            work = os.listdr(file_dr)
            print(work)
            continue
         
         elif 'How are you' in query:
            speak("I am fine. What about you")
         elif 'who created you' in query:
            speak("WOLVES: AKHIL SINGH AND RISHI RAJ VERMA")
            continue
         elif 'when you were born' in query:
            speak("I am still in progress, I havent taken birth properly")
            continue
         elif 'where you were born' in query:
            speak("In School of computer engineering campus")
            continue
         elif 'what do you like to do' in query:
            speak("Serving my master is the most enjoyable thing for me")
            continue
         
   
         elif 'good morning bunty' in query :
            speak("good morning, master have a beautifu day ahead")
            continue
         elif 'good afternoon bunti' in query :
            speak("good afternoon, master")  
            continue
         elif 'good evening bunti' in query :
            speak("good evening, master")  
            continue        
         elif 'good night bunti' in query :
            speak("good night, master")
            continue  
         elif 'who is your favourite superhero' in query :
            speak("Iron man, love you 3000")
            continue
       
       
         elif 'which is your favourite movie' in query :
            speak("I don't watch movies very often but Interstellar is my favourite")
            continue
     
         elif 'open telegram' in query: 
            pyttsx3.speak("Opening Telegram") 
            print(".") 
            print(".") 
            telegram_path = '"C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_5.10.3.0_x64__t4vj0pshhgkwm\\Telegram.exe"' 
            os.system(telegram_path) 
            continue
            #######

         elif 'open file explorer' in query:
            file_dr='C:\\Users\\KIIT\\Documents'
            work = os.listdr(file_dr)
            print(work)
            os.startfiles(os.path.join(file_dr, work[1]))
            continue
           
         elif 'open mail' in query :
            pyttsx3.speak("opening mail")
            print(".")
            print(".")
            os.system("mail.exe")
            continue
         elif 'what do you do in your free time' in query :
            speak("just relax in your system")  
            continue
         elif 'open microsoft store' in query :
            pyttsx3.speak("opening windows store")
            print(".")  
            print(".")
            os.system("microsoftstore.exe")
            continue
         elif 'open wps office' in query :
            pyttsx3.speak("opening wps office")
            print(".")  
            print(".")
            os.system("wpsoffice.exe")
            continue
         elif 'do you watch anime' in query :
            speak("yes, some of my favourites are demon slayer, Attack on Titan and death note")
            continue
         elif 'open discord' in query :
            speak("opening discord")
            webbrowser.open("discord.com")
            continue
         elif 'open reddit' in query :
            speak("opening reddit")
            webbrowser.open("reddit.com")  
            continue
