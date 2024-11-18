3:00 AM i have changed the whole code beause "sapi" cannot work in my macbook
so have just blackboxed the whole code but it is working but 
not taking mic request 
 



 03:07 AM 
     if __name__ == "__main__":
    speak() # calling the function
    off 






03:17 AM 




import pyttsx3

def initialize_engine():
    engine = pyttsx3.init()  # On Mac, you don't need to specify "sapi5"
    
    voices = engine.getProperty('voices')
    
    for voice in voices:
        if 'female' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
   
    engine.setProperty('rate', 150)  
    
    engine.setProperty('volume', 0.7)  
    
    return engine

def speak(text="Hello, how are you?"):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command(text):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
