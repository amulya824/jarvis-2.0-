import speech_recognition as sr
import os
import webbrowser


def say(text):
    os.system(f'say "{text}"')  # Added quotes around the text


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User  said: {query}")  # Print recognized text
            return query
        except Exception as e:
            print(f"Error: {e}")  # Print error for debugging
            return "Some error occurred"


if __name__ == '__main__':
    print('FRIDAY')
    say("Hello I am FRIDAY")
    while True:
        print("Listening...")
        text = takeCommand()
        print(f"Recognized Text: {text}")  # Print recognized text for verification

        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["spotify", "spotify"],
            ["facebook", "https://www.facebook.com"],
            ["instagram", "https://www.instagram.com"],
            ["twitter", "https://www.twitter.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["amazon", "https://www.amazon.com"],
            ["reddit", "https://www.reddit.com"],
            ["github", "https://www.github.com"],
            ["netflix", "https://www.netflix.com"]
        ]

        opened = False  # Flag to check if a site was opened
        for site in sites:
            if f"open {site[0]}" in text.lower():  # Ensure the check is case insensitive
                if site[0] == "spotify":
                    say(f"Opening {site[0]} sir...")
                    os.system("open -a Spotify")  # Special handling for Spotify
                else:
                    say(f"Opening {site[0]} sir...")
                    webbrowser.open(site[1])
                opened = True
                break  # Exit the loop once a site is opened

        if not opened and "exit" in text.lower():  # Optional: Exit condition
            say("Goodbye!")
            break
