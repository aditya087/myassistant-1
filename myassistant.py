import os
import pyttsx3

pyttsx3.speak("Hi there, Welcome to your personal assistant")

while True:
    pyttsx3.speak("What do you want to run")
    print("What do you want to run:", end = '')
    r = input()
    
    if (('run' in r) or ('start' in r) or  ('open' in r) or ('execute' in r)) and (('chrome' in r) or ('browser' in r)):
        pyttsx3.speak("opening google chrome for you")
        os.system("start chrome")
                                                                                    
    elif (('run' in r) or ('start' in r) or ('open' in r) or ('execute' in r)) and (('media' in r) or ('player' in r) or ('windows media player' in r)):
        pyttsx3.speak('opening windows media player for you')
        os.system('start wmplayer')
        
    elif (('run' in r) or ('start' in r)  or ('open' in r) or ('execute' in r)) and (('notepad' in r) or ('notebook' in r) or ('text editor' in r)):
        pyttsx3.speak("opening notepad for you")
        os.system('start notepad')
        
    elif (('run' in r) or ('start' in r) or ('open' in r) or ('execute' in r)) and ('paint' in r):
        pyttsx3.speak('opening paintfor you')
        os.system('start mspaint')
        
    elif (('run' in r) or ('start' in r) or ('open' in r) or ('execute' in r)) and (('cmd' in r) or ('command prompt' in r) or ('command' in r)):
        pyttsx3.speak('opening command prompt for you')
        os.system('start cmd.exe')

    elif (('run' in r) or ('start' in r)  or ('open' in r) or ('execute' in r)) and (('cp' in r) or ('control' in r) or ('control panel' in r)):
        pyttsx3.speak('opening control panel for you')
        os.system('start control panel')      
                
    elif (('run' in r) or ('start' in r)  or ('open' in r) or ('execute' in r)) and (('calculator' in r) or ('calc' in r)):
        pyttsx3.speak('opening calculator for you')
        os.system('start calc')

    elif (('run' in r) or ('start' in r) or ('open' in r) or ('execute' in r)) and (("excel" in r) or ('microsoft excel') in r ):
        pyttsx3.speak('opening microsoft excel for you')
        os.system('start excel.exe')

    elif (('run'in r) or ('start' in r) or ('open' in r) or ('execute' in r)) and (('power point' in r) or ('microsoft power point' in r)):
        pyttsx3.speak('opening microsoft powerpoint for you')
        os.system('start powerpnt')

    elif (('run'in r) or ('start' in r) or ('open' in r) or ('execute' in r)) and (('explorer' in r) or ('internet explorer' in r)):
        pyttsx3.speak('opening internet explorer for you')
        os.system('start iexplore')

    elif (('stop' in r) or ('exit' in r) or ('quit' in r) or ('close' in r)):
        pyttsx3.speak('Thank you')
        break

    else:
        pyttsx3.speak("Don't support, Try again!")
        print("Don't support, Try again!")
