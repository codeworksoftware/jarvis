#Paketler--->
import datetime
from datetime import datetime
import time
import speech_recognition as sr
import webbrowser
import random
import pyttsx3
import os
from googletrans import Translator
import keyboard

translator = Translator()

#Mikrofon-Kurulumu--->
r = sr.Recognizer()
ArduinoUnoSerial = serial.Serial('COM4',9600)
spaid = 0
this_app = ""
ai_mode = "voice"

#Mikrofon-Motoru--->
def record(ask=False):
    global spaid, voice
    with sr.Microphone() as source:
        try:
            r.adjust_for_ambient_noise(source, duration=0.1)
            r.energy_threshold = 100
            r.dynamic_energy_threshold = True
            r.dynamic_energy_ratio = True
            if ask:
                speak(ask)
            voice = ''
            audio = r.listen(source)
            voice = r.recognize_google(audio, language="en-US")
        except sr.UnknownValueError:
            if voice == "":
                ...
            else:
                listses = ("I don't have what you're looking for.","Sorry, I can't understand you.","I can't understand you.")
                rica = random.choice(listses)
                print("Jarvis: "+rica+"\n")
                speak(rica)
        except r:
            ...
        except sr.WaitTimeoutError:
            ...
        except TypeError:
            ...
        return voice

#Konuşma-Motoru--->
def speak(say_to_text):
    converter = pyttsx3.init()
    converter.setProperty("rate", 180)
    converter.setProperty("volume", 1)
    voices = converter.getProperty('voices')
    converter.setProperty('voice', voices[1].id)
    converter.say(say_to_text)
    converter.runAndWait()

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def loading_bar():
    items = list(range(0, 50))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

def back_up_system():
    backup = open("jarvis.py","r",encoding="utf-8")
    backups = open("backed_up_system.jarvis","w",encoding="utf-8")
    print("Jarvis: The system is backing up.")
    speak("the system is backing up.")
    print()
    for i in backup.readlines():
        print(">>> "+i)
        backups.write(i)
        time.sleep(0.025)
    backup.close()
    backups.close()
    print("Jarvis: The system is backed up.")
    speak("the system is backed up.")
    print()
    print("Jarvis: System codes are being checked.")
    speak("system codes are being checked.")
    os.system("cls")
    loading_bar()
    os.system("cls")
    print("-"*60+"Jarvis"+"-"*60)
    check_file = open("jarvis.py","r",encoding="utf-8")
    checked_file = open("backed_up_system.jarvis","r",encoding="utf-8")
    if check_file.read() != checked_file.read():
        print("Jarvis: The codes did not match correctly.")
        speak("the codes did not match correctly.")
        recovery()
    else:
        print("Jarvis: System checked.")
        speak("system checked.")
        time.sleep(0.2)
        os.system("cls")
        print("-"*60+"Jarvis"+"-"*60)

def recovery():
    global ai_mode
    os.system("cls")
    print("-"*57+"Jarvis"+"-"*57)
    os.system("color 4")
    print("Jarvis: System encountered an error. The system is rebooting. Just a few seconds.")
    speak("system encountered an error. the system is rebooting. just a few seconds.")
    remove = open("jarvis.py","w",encoding="utf-8")
    remove.write("")
    remove.close()
    backup = open("backed_up_system.jarvis","r",encoding="utf-8")
    backups = open("main.py","a+",encoding="utf-8")
    a = 1
    for i in backup.readlines():
        print(str(a)+"-  "+i)
        backups.write(i) and time.sleep(0.05)
        a = a + 1
    backup.close()
    backups.close()
    print("Jarvis: The system has been recovered.")
    speak("the system has been recovered.")
    os.system("cls")
    print("Jarvis: System codes are being checked.")
    speak("system codes are being checked.")
    loading_bar()
    check_file = open("backed_up_system.jarvis","r",encoding="utf-8")
    checked_file = open("main.py","r",encoding="utf-8")
    if check_file.read() != checked_file.read():
        recovery()
    else:
        print("Jarvis: System checked. Now reboot the system.")
        speak("checked. now reboot the system.")
        exit()

os.system("cls")
print("-"*57+"Jarvis"+"-"*57)
os.system("color 4")
try:
    #İşlem-Merkezi
    def response(voice):
        global ai_mode
        if "i want to write" == voice or "i want to write for speak" == voice:
            print("Jarvis: OK!")
            speak("OK!")
            voice = input("User: ")
        if "change mode" == voice:
            if ai_mode == "voice":
                ai_mode = "text"
            elif ai_mode == "text":
                ai_mode = "voice"
        if "jarvis" in voice or "hey jarvis" in voice:
            listses = ("sir!","listen you","speak anything")
            rica = random.choice(listses)
            print("Jarvis: "+rica+".")
            speak(rica)
        if "who is friday" in voice:
            print("Jarvis: Friday is my sister.")
            speak("Friday is my sister.")
        if "how are you" in voice:
            print("Jarvis: I am fine thank you, and you?")
            speak("i am fine thank you, and you?")
            while True:
                if "mee to" in voice:
                    print("Jarvis: I am pleased.")
                    speak("i am pleased")
                elif "thank you" in voice:
                    print("Jarvis: I am pleased.")
                    speak("i am pleased")
                elif "thank you" in voice and "mee to" in voice:
                    print("Jarvis: I am pleased.")
                    speak("i am pleased")
                else:
                    break
        if voice == "hi":
            speak("hi! welcome!")
        if "what time is it" in voice:
            watch = datetime.now().strftime('%H:%M')
            print("Jarvis: "+watch)
            speak(watch)
        if "thank you" in voice:
            listses = ("you're welcome","please!","ok bro","not problem")
            rica = random.choice(listses)
            print("Jarvis: "+rica)
            speak(rica)
        elif "i am fine" in voice:
            print("Jarvis: Good news!")
            speak("good news!")
        if "open" in voice:
            try:
                voice = voice.replace("open ","")
                global this_app
                this_app = voice
                if "spotify" in voice:
                    os.startfile(f"C:\\Users\\pc\\AppData\\Roaming\\Spotify\\Spotify.exe")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "google" in voice:
                    os.startfile(f"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "edge" in voice:
                    os.startfile(f"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "visual" in voice or "visual studio" in voice or "code" in voice:
                    os.startfile(f"C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "instagram" in voice:
                    webbrowser.open_new_tab("https://www.instagram.com/firattunaarslann")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "youtube" in voice:
                    webbrowser.open_new_tab("https://youtube.com")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "file manager" in voice:
                    os.startfile("C:\\")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "volorant" in voice:
                    os.startfile(f"C:\\Users\\pc\\OneDrive\\Masaüstü\\Oyunlar\\VALORANT.lnk")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "whatsapp" in voice:
                    webbrowser.open_new_tab("https://web.whatsapp.com")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "facebook" in voice:
                    webbrowser.open_new_tab("https://www.facebook.com")
                    print("jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                if "my channel" in voice:
                    webbrowser.open("https://www.youtube.com/channel/UCMAOZBamAkIC9hSqb4TFx0Q")
                    print("Jarvis: "+voice+" starting.")
                    speak(voice+" starting.")
                elif voice not in ["spotify","google","edge","youtube","instagram","visual","visual studio","code","file maneger","valorant","whatsapp","console","my channel","facebook"]:
                    print("jarvis: Is not such app.")
                    speak("is not such app.")

            except:
                print("Jarvis: Is not such app.")
                speak("is not such app.")
        if "is not starting" in voice:
            print("Jarvis: OK! I am try again.")
            speak("okey. i am try again.")
            time.sleep(1)
            try:
                if "spotify" in this_app:
                    os.startfile(f"C:\\Users\\pc\\AppData\\Roaming\\Spotify\\Spotify.exe")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "google" in this_app:
                    os.startfile(f"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "edge" in this_app:
                    os.startfile(f"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "visual" in this_app or "visual studio" in this_app or "code" in this_app:
                    os.startfile(f"C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "instagram" in this_app:
                    webbrowser.open_new_tab("https://www.instagram.com/firattunaarslann")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "youtube" in this_app:
                    webbrowser.open_new_tab("https://youtube.com")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "file manager" in this_app:
                    os.startfile("C:\\")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "volorant" in this_app:
                    os.startfile(f"C:\\Users\\pc\\OneDrive\\Masaüstü\\Oyunlar\\VALORANT.lnk")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "whatsapp" in this_app:
                    webbrowser.open_new_tab("https://web.whatsapp.com")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "facebook" in this_app:
                    webbrowser.open_new_tab("https://www.facebook.com")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                if "my channel" in this_app:
                    webbrowser.open("https://www.youtube.com/channel/UCMAOZBamAkIC9hSqb4TFx0Q")
                    print("Jarvis: "+this_app+" starting...")
                    speak(this_app+" starting...")
                elif this_app not in ["spotify","google","edge","youtube","instagram","visual","visual studio","code","file maneger","valorant","whatsapp","console","my channel","facebook"]:
                    print("jarvis: Is not such app.")
                    speak("is not such app.")
            except:
                print("Jarvis: Is not such app.")
                speak("is not such app.")
        if "search photo for" in voice:
            voice = voice.replace("search photo ","")
            print("Jarvis: Searching for related photos.")
            speak("Searching for related photos.")
            url = "https://www.google.com/search?q="+voice+"&sxsrf=APq-WBtVbjq7JEbLkW-O_vs71Q2Emtc_DQ:1643443637317&source=lnms&tbm=isch&sa=X&sqi=2&ved=2ahUKEwiJl9fRwNb1AhXILLkGHYHcBA8Q_AUoBHoECAEQBg&biw=1920&bih=961&dpr=1"
            webbrowser.open(url)
        elif "search" in voice:
            voice = voice.replace("search ","")
            if "in the youtube" in voice:
                voice = voice.replace("in the youtube","")
                speak("looking for "+voice+" in the youtube")
                webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+voice)
            elif "in the spotify" in voice:
                voice = voice.replace("in the spotify","")
                webbrowser.open_new_tab("https://open.spotify.com/search/"+voice)
            elif "in the google" in voice:
                voice = voice.replace("in the google","")
                webbrowser.open_new_tab("https://www.google.com/search?q="+voice)
            elif "in the bing" in voice:
                voice = voice.replace("in the bing","")
                webbrowser.open_new_tab("https://www.bing.com/search?q="+voice)
            else:
                speak("looking for "+voice)
                webbrowser.open_new_tab("https://www.google.com/search?q="+voice)
        if voice == "how's the weather":
            speak("looking at the weather of trabzon")
            webbrowser.open_new_tab("https://www.accuweather.com/tr/tr/trabzon/321281/daily-weather-forecast/321281?day=1")
        if "what is your gender" == voice:
            print("jarvis: My gender is male.")
            speak("my gender is male.")
        if "hello" in voice:
            print("Jarvis: Hello sir!")
            speak("hello sir!")
            while True:
                print()
                voice = record().lower()
                print("User: "+voice)
                if "i am fine thank you" in voice:
                    print("Jarvis: You're welcome!")
                    speak("you're welcome")
                    break
                if "and you" in voice:
                    print("Jarvis: I am fine too.")
                    speak("i am fine too")
                    break
                else:
                    break
        if "show system" in voice or "show your system" in voice or "your system" in voice:
            print("Jarvis: I am showing system now.")
            speak("i am showing system now.")
            print()
            codes = open("jarvis.py","r",encoding="utf-8")
            for i in codes.readlines():
                print(">>>  "+i)
                time.sleep(0.025)
            codes.close()
            print("Jarvis: I am showed the system.")
            speak("i am showed the system.")
        if "backup system" in voice:
            back_up_system()
        if "restart" == voice or "inception" == voice or "go inception" in voice:
            os.system("python jarvis.py")
        if "who are you" in voice or "who is jarvis" in voice:
            print("Jarvis: Jarvis is a personal voice assistant produced in Turkey.")
            speak("jarvis is a personal voice assistant produced in turkey.")
            print("        Date of birth 11.12.2021.")
            speak("date of birth 11.12.2021.")
            print("        Its creator is CodeWork.")
            speak("it is creator is code work.")
        if "where are you from" in voice:
            print("Jarvis: I am from Turkey.")
            speak("i am from turkey")
        if "can you talk to me" in voice or "can you talk for me" in voice:
            print("Jarvis: Yeah bro. How are you?")
            speak("yeah bro, how are you?")
        if voice == "shut this application":
            keyboard.press_and_release("alt + f4")
        if "i love you" in voice:
            print("Jarvis: I love you too. so glad that I have you.")
            speak("i love you too. so glad that I have you.")
        if "can you do sports" == voice:
            print("Jarvis: No, because I don't have a body.")
            speak("no, because i don't have a body.")
        if "where are you" in voice:
            print("Jarvis: I'm inside CodeWork's cloud-based storage system.")
            speak("i'm inside code work's cloud-based storage system.")
        if "what day is it today" in voice or "this day" in voice:
            x = datetime.now()
            gün = x.strftime("%A")
            print("Jarvis: "+gün+".")
            speak(gün)
        if "what month are we in" in voice or "this month" in voice:
            x = datetime.now()
            ay = x.strftime("%B")
            print("Jarvis: "+ay+".")
            speak(ay)
        if "what is your name" in voice:
            print("Jarvis: My name is Jarvis.")
            speak("my name is jarvis")
        if "i want to" in voice:
            voice = voice.replace("i want to","")
            if "watch" in voice:
                voice = voice.replace(("watch",""),"")
                print("")
                if "in the youtube" in voice:
                    voice = voice.replace("youtube","")
                    webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+voice)
            if "play" in voice:
                voice = voice.replace("play","")
                if "minecraft" in voice:
                    os.startfile(f"C:\\Users\\pc\\OneDrive\\Masaüstü\\Minecraft.lnk")
                    print("Jarvis: Minecraft starting.")
                    speak("minecraft starting.")
                if "valorant" in voice:
                    os.startfile(f"C:\\Users\\pc\\OneDrive\\Masaüstü\\VALORANT.lnk")
                    print("Jarvis: VALORANT starting.")
                    speak("valorant starting.")
        if "wait" in voice:
            print("Jarvis: OK! I am waiting to you.")
            speak("okey! i am waiting to you.")
            while True:
                sleep = record().lower()
                if "jarvis" in sleep:
                    spaid = 0
                    print("Jarvis: I'm listening sir")
                    speak("i'm listening sir")
                    break
        if "i am here" in voice or "i am coming" in voice:
            print("Jarvis: OK! Sir, I am listen you!")
            speak("okey! sir, i am listen you!")
        if "system check" in voice:
            loading_bar()
            print("Jarvis: System checked.")
            speak("system checked.")
        elif "shut down my computer" == voice or "shut down" == voice or "shut dowm this computer" == voice or "shut down computer" == voice:
            print("Jarvis: Shutdowning your computer now.")
            speak("shutdowning your computer now.")
            time.sleep(1)
            os.system("shutdown /s /t 1")
        if "change my name" in voice or "can you change my name" in voice or "can i change my name" in voice:
            print("Jarvis: Of Course! From now on how would you like me to call you?")
            speak("of course! from now on how would you like me to call you?")
            print()
            while True:
                new_name = record().lower()
                print("User: "+new_name+".")
                if new_name == "i want to write my name" or "i want to write" == new_name or "i want to my new name" == new_name:
                    print("Jarvis: OK!")
                    speak("okey!")
                    new_name = input("Your new name: ")
                    new_naming = open("user_name.jarvis","w",encoding="utf-8")
                    new_naming.write(new_name)
                    new_naming.close()
                    print("Jarvis: Hello, "+new_name+"!")
                    speak("hello, "+new_name+"!")
                    break
                elif new_name != "":
                    new_naming = open("user_name.jarvis","w",encoding="utf-8")
                    new_naming.write(new_name)
                    new_naming.close()
                    print("Jarvis: Hello, "+new_name+"!")
                    speak("hello, "+new_name+"!")
                    break
                else:
                    print("Jarvis: I wait to you.")
                    speak("i wait to you")
                    continue
        elif "what is my name" in voice or "my name" in voice:
            named = open("user_name.jarvis","r",encoding="utf-8")
            namesd = named.read()
            named.close()
            print("Jarvis: Your name is "+namesd+".")
            speak("your name is "+namesd+".")
        if "sleep" in voice:
                print("Jarvis: I am sleeping.")
                speak("i am sleeping")
                time.sleep(0.5)
                print("System: Sleeping. Call him by name to wake him up.")
                while True:
                    sleep = record().lower()
                    if "jarvis" in sleep or "wake up" in sleep:
                        spaid = 0
                        speak("okey!... listen you...")
                        break
        if "how old am i" in voice:
            od = open("user_old.jarvis","r",encoding="utf-8")
            print("Jarvis: Your old is "+od.read())
            speak("your old is "+od.read())
            od.close()
        if voice in ["can you change my old","can i change my old","change my old"]:
            print("Jarvis: Of course!")
            speak("Of course!")
            time.sleep(0.50)
            print("Jarvis: Say your new old.")
            speak("Say your new old.")
            print()
            while True:
                a = 0
                new_old = record().lower()
                if new_old != "":
                    print("User: "+new_old)
                    olds = open("user_old.jarvis","w",encoding="utf-8")
                    olds.write(new_old)
                    olds.close()
                    print("Jarvis: Your age has been successfully changed.")
                    speak("Your age has been successfully changed.")
                    print()
                    break
                else:
                    a = a+1
                    if a == 3 or a == 6 or a == 9:
                        print("Jarvis: I wait to you.")
                        speak("i wait to you.")
                        continue
                    else:
                        break
        if voice in ["can you help me","help me","help"]:
            print("Jarvis: How can I help you?")
            speak("How can I help you?")
            print()
            print("Jarvis: Look screen.")
            speak("Look screen.")
            print()
            print()
            print("----------HELP-LIST---------")
            time.sleep(0.25)
            print("1- How can I change my name?")
            time.sleep(0.25)
            print("2- How can I change my old?")
            time.sleep(0.25)
            print()
            a = 0
            while True:
                helps = record().lower()
                if helps == "":
                    continue
                else:
                    print("User: "+helps)
                    if "how can i change my name" == helps:
                        print("Jarvis: Say 'change my name'.")
                        speak("Say 'change my name'.")
                        break
                    if "how can i change my old" == helps:
                        print("Jarvis: Say 'change my old'.")
                        speak("Say 'change my old'.")
                        break
                    else:
                        a = a+1
                        if a == 3 or a == 6 or a == 9:
                            print("Jarvis: I wait to you.")
                            speak("i wait to you.")
                            continue
                        else:
                            break
        if "are you bored" in voice:
            print("Jarvis: Unless you're here, yes, I get bored.")
            speak("Unless you're here, yes, I get bored.")
        if "what can you do" in voice:
            print("jarvis: I can speak to you.")
            speak("i can speak to you.")
        if "create assistant" in voice or "create new assistant" in voice:
            print("Jarvis: What's the name of the new assistant?")
            speak("What's the name of the new assistant?")
            assistant_name = input("User: Assistant name is ")
            os.makedirs(assistant_name)
            print("Jarvis: What's the gender of the new "+assistant_name+"?")
            speak("What's the gender of the "+assistant_name+"?")
            males = input("[System]: Famele or Male? (f/M)")
            if males == "f":
                mal = "[0]"
            elif males == "M":
                mal = "[1]"
            lower_assistant_name = assistant_name.lower()
            print("Jarvis: OK! I am starting.")
            speak("OK! I am starting.")
            jar = open(assistant_name+f"\\"+assistant_name+".py","a+",encoding="utf-8")
            jarjar = open("jarvis.py","r",encoding="utf-8")
            for i in jarjar.readlines():
                print(">>> "+i)
                jar.write(i)
                time.sleep(0.02)
            jar.close()
            jarjar.close()
            print("Jarvis: It's being adapted for Jarvis to "+assistant_name+".")
            speak("It's being adapted for Jarvis to "+assistant_name+".")
            loading_bar()
            jars = open(assistant_name+"/"+assistant_name+".py","r",encoding="utf-8")
            jarss = jars.read()
            jarss = jarss.replace("Jarvis",assistant_name)
            jarss = jarss.replace("jarvis",lower_assistant_name)
            jarss = jarss.replace("[1]",mal)
            jars.close()
            jarsss = open(assistant_name+"/"+assistant_name+".py","w",encoding="utf-8")
            jarsss.write(jarss)
            time.sleep(2)
            print("Jarvis: Yes! "+assistant_name+" is finished.")
            backs = open(assistant_name+"/backed_up_system."+lower_assistant_name,"w",encoding="utf-8")
            backs.close()
            user_name = open(assistant_name+"/user_name."+lower_assistant_name,"w",encoding="utf-8")
            user_name.close()
            user_old = open(assistant_name+"/user_old."+lower_assistant_name,"w",encoding="utf-8")
            user_old.close()
            setup_codes = open("setup.code","r",encoding="utf-8")
            setup_code = setup_codes.read()
            setup_codes.close()
            setup_code = setup_code.replace("lower_assistant_name",lower_assistant_name)
            setup_code = setup_code.replace("assistant_name",assistant_name)
            print(setup_code)
            setup_file = open(assistant_name+"/setup.bat","w",encoding="utf-8")
            setup_file.write(setup_code)
            speak("Yes! "+assistant_name+" is finished.\n")
        if "what is your speed" in voice:
            print("Jarvis: My speaking rate is set to 180 from 100 to 200.")
            speak("My speaking rate is set to 180 from 100 to 200.")
        if "can i change your speaking rate" in voice or "can you change your speaking rate" in voice or "change your speaking rate" in voice:
            print("Jarvis: Unfortunately no, only developers can change this, but this is among the upcoming updates.")
            speak("Unfortunately no, only developers can change this, but this is among the upcoming updates.")
        if voice in ["pink","red","orange","orange","yellow","green","blue","purple","black","brown","white","gray"]:
            print("Jarvis: "+voice+" is a color.")
            speak(voice+" is a color.")
        if "what the capital of" in voice or "what's the capital of " in voice:
            ülkeler = {
                "japan":"Tokyo",
                "south korea":"Seul",
                "north korea":"Pyongyang",
                "america":"New York",
                "turkey":"Ankara",
                "russia":"Moscow",
                "china":"Beijing",
                "africa":"There are three capitals in South Africa: Pretoria, the executive capital, Cape Town, the legislative capital, and Bloemfontein, the judicial capital.",
                "canada":"Ottava",
                "australia":"Kanberra",
                "german":"Berlin",
                "italia":"Roma",
                "france":"Londra",
                "spain":"Madrid",
                "portugal":"Lizbon",
                "holland":"Amsterdam",
                "austria":"Viyana",
                "greece":"Atina",
                "belgium":"Brüksel",
                "ireland":"Dublin",
                "finland":"Helsinki",
                "qatar":"Doha",
                "arabia":"Riyad",
                "palestine":"Kudüs",
                "syria":"Şam",
                "mexico":"Mexico",
                "antartica":"None",
                "albania":"Tiran",
                "mongolia":"Ulanbator",
                "kazakhistan":"Nur-Sultan",
                "azerbaijan":"Bakü",
                "lithuania":"Vilnius",
                "slovakia":"Bratislava",
                "malta":"Valetta",
                "monaco":"Monaco",
                "cyprus":"Lefkoşa",
                "luxembourg":"Lüksemburg",
                "montenegro":"Podgoritsa",
                "kosovo":"Priştine",
                "andorra":"Andorra la Vella",
                "vatican":"Vatican",
                "latvia":"Riga",
                "slovenia":"Lübliyana",
                "estonia":"Tallin",
                "guadeloupe":"Basse-Terre",
                "san marino":"San Marino",
                "reunion":"Saint-Denis",
                "martinis":"None",
                "saint barthelemy":"Gustavia",
                "mayotte":"Mamoudzou",
                "saint martin":"Philipsburg",
                "brazil":"brazil",
                "turkmenistan":"Aşkabat",
                "north cyprus":"Lefkoşa Turkish Municipality",
                "iranian":"Tahran",
                "yemen":"Sana",
                "moritania":"Nuakşot",
                "pakistan":"Islamabat"
            }
            voice = voice.replace("what the capital of ","")
            voice = voice.replace("what's the capital of ","")
            if voice in ülkeler:
                print("Jarvis: "+ülkeler[voice])
                speak(ülkeler[voice])
            else:
                print("Jarvis: The "+voice+" is not registered in the system.")
                speak("The "+voice+" is not registered in the system.")
        if voice == "exits" or voice == "goodbye" or voice == "exit":
            exitss = ("goodbye","see you later","take care")
            a = random.choice(exitss)
            print("Jarvis: OK, "+a)
            speak(a+".")
            exit()
except:
    recovery()
#Dinleme-Modülü
clock = datetime.now()
saat = clock.strftime("%H")
dakika = clock.strftime("%M")
hemsaathemdakika = clock.strftime("%H:%M")

named = open("user_name.jarvis","r",encoding="utf-8")
namesd = named.read()
named.close()

def start_jarvis(namess=namesd):
    global spaid, ai_mode
    if int(saat) <= 12:
        print("Jarvis: Good morning "+namess+". I am listen you.")
        speak("good morning "+namess+". i am listen you.")
        print()
    elif int(saat) >= 12 and int(saat) <= 17:
        print("Jarvis: Good afternoon "+namess+". I am listen you.")
        speak("good after noon "+namess+". i am listen you.")
        print()
    elif int(saat) >= 17:
        print("Jarvis: Good night "+namess+". I am listen you.")
        speak("good night "+namess+". i am listen you.")
        print()
    while True:
        if ai_mode == "voice":
            voice = record().lower()
        elif ai_mode == "text":
            voice = input("User:")
        if voice == "":
            spaid = spaid+1
        else:
            if "clear screen" in voice or "clear console" in voice:
                speak("screen is crearning")
                os.system("cls")
                print("-"*57+"Jarvis"+"-"*57)
                os.system("color 4")
                continue
            elif ai_mode == "voice":
                print("User: "+voice)
                time.sleep(0.3)
                response(voice)
            else:
                time.sleep(0.3)
                response(voice)
            print()
            continue
        if spaid == 6:
            print("Jarvis: Are you here "+namesd+"?")
            speak("are you here "+namesd+"?")
        if spaid >= 7 or "sleep" in voice:
            print("Jarvis: I am sleeping.")
            speak("i am sleeping")
            time.sleep(0.5)
            print("System: Sleeping. Call him by name to wake him up.")
            while True:
                sleep = record().lower()
                if "jarvis" in sleep or "wake up" in sleep:
                    spaid = 0
                    speak("okey!... listen you...")
                    break
        else:
            continue

def intros():
    while True:
        namess = record().lower()
        if namess != "":
            if "name" in namess:
                namess = namess.replace("name ","")
            if "my" in namess:
                namess = namess.replace("my ","")
            if "is" in namess:
                namess = namess.replace("is ","")
            namds = open("user_name.jarvis","w",encoding="utf-8")
            namds.write(namess)
            namds.close()
            break
        else:
            continue
    while True:
        print("Jarvis: OK! How old are you "+namess+"?")
        speak("OK! How old are you "+namess+"?")
        old = record().lower()
        if old != "":
            olds = open("user_old.jarvis","w",encoding="utf-8")
            olds.write(old)
            olds.close()
            os.system("cls")
            print("---\n---\n[SYSTEM]: Just a few seconds, the registration process is completed.")
            time.sleep(1)
            print("[SYSTEM]: Editing system files.")
            time.sleep(1)
            print("[SYSTEM]: ['user_name.jarvis','w+r+a+',encoding='utf-8']: Completed.")
            time.sleep(0.5)
            print("[SYSTEM]: ['user_old.jarvis','w+r+a+',encoding='utf-8']: Completed.")
            time.sleep(2)
            os.system("Jarvis.py")
        else:
            continue
            

dsa = open("user_name.jarvis","r",encoding="utf-8")
namesds = dsa.read()
dsa.close()

if namesds == "":
    print("jarvis: Hello! What is your name?")
    speak("hello! What is your name?")
    intros()
else:
    start_jarvis()
