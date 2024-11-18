import speech_recognition as sr
import os
import webbrowser
import feedparser
import pyttsx3
import threading
#import requests
import aifc
import pyaudio

# Global variable to control speaking
stop_speaking = False

def say(text):
    global stop_speaking
    stop_speaking = False  # Reset the stop flag
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.5)  # Volume (0.0 to 1.0)

    # Speak each word
    for word in text.split('. '):
        if stop_speaking:  # Check if we should stop speaking
            print("Speech interrupted.")
            break
        engine.say(word)
        engine.runAndWait()  # Wait for speech to finish before continuing

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User   said: {query}")  # Print recognized text
            return query
        except Exception as e:
            print(f"Error: {e}")  # Print error for debugging
            return "Some error occurred"

def aggregate_news(feed_url):
    """Fetches and aggregates news from the provided RSS feed URL."""
    try:
        feed = feedparser.parse(feed_url)
        titles = []
        
        # Check if the feed has entries
        if not feed.entries:
            print("No news available.")
            return []

        # Get the latest 5 news articles
        for entry in feed.entries[:5]:
            title = entry.title
            titles.append(title)

        return titles
    
    except Exception as e:
        print(f"Failed to aggregate news: {e}")
        return []

def listen_for_friday():
    """Listens for the command 'FRIDAY' to interrupt current actions."""
    global stop_speaking
    while True:
        text = takeCommand()
        if "friday" in text.lower():  # Check if the command is 'FRIDAY'
            print("FRIDAY command received. Stopping current action...")
            stop_speaking = True  # Set the flag to stop speaking
            return  # Exit the listening loop

def main():
    print('FRIDAY')
    say("Hello I am FRIDAY")
    
    while True:
        print("Listening...")
        text = takeCommand()
        print(f"Recognized Text: {text}")  # Print recognized text for verification
        
        # Check for the 'FRIDAY' command
        if "friday" in text.lower():
            print("FRIDAY command received. Stopping current action...")
            threading.Thread(target=listen_for_friday).start()
            continue  # Restart the loop to listen for new commands

        # Check if the user asked for news
        if "news" in text.lower():
            news_feed_url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"  # Replace with a valid RSS feed URL
            news_titles = aggregate_news(news_feed_url)
            if news_titles:
                for title in news_titles:
                    say(title)
            else:
                say("No news available.")
            continue  # Restart the loop to listen for new commands

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
            if f"open {site[0]}" in text.lower():
                if site[0] == "spotify":
                    os.system("open -a Spotify")  # Use os.system for Spotify
                else:
                    webbrowser.open(site[1])  # Use webbrowser.open for websites
                opened = True
                break  # Exit the loop after opening a site

        if not opened:
            say("Sorry, I didn't understand that command.")  # Respond if no valid command was recognized

if __name__ == "__main__":
    main()
