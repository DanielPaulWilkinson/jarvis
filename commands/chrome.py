import webbrowser
import speech

chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'


def openChrome(engine):
    engine.say('On it!')
    webbrowser.open(chrome_path)
    engine.say('Sir, I\'ve opened chrome')


def openFacebook(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://www.facebook.com/')
    engine.runAndWait()


def openTwitter(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://twitter.com/home?lang=en-gb')
    engine.runAndWait()


def openLinkedIn(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://www.instagram.com/?hl=en')
    engine.runAndWait()


def openAmazion(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://www.amazon.co.uk/')
    engine.runAndWait()


def openNetflix(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://www.netflix.com/browse')
    engine.runAndWait()


def openInstagram(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://www.linkedin.com/feed/')
    engine.runAndWait()


def openYoutube(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://www.youtube.com/')
    engine.runAndWait()


def openRReddit(engine):
    engine.say('Sure Thing!')
    webbrowser.open_new_tab('https://www.reddit.com/')
    engine.runAndWait()


def openSocials(engine):
    engine.say('Sure Thing!')
    engine.runAndWait()
    webbrowser.open_new_tab('https://www.instagram.com/?hl=en')
    webbrowser.open_new_tab('https://twitter.com/home?lang=en-gb')
    webbrowser.open_new_tab('https://www.linkedin.com/feed/')
    webbrowser.open_new_tab('https://www.facebook.com/')
    engine.say(
        'Sir, I\'ve opened all of you socials. Would you like me to open your emails as well?')
    engine.runAndWait()
    answer = speech.takeCommand()
    if "yes" or "yeah" or "sure" in answer:
        webbrowser.open_new_tab('https://mail.google.com/mail/')
    else:
        engine.say('No Problem!')
        engine.runAndWait()
    engine.say('Enjoy!')
    engine.runAndWait()
