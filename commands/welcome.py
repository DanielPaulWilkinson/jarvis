import datetime


def launch(engine):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Good Morning Sir! how may I help you?")
        engine.runAndWait()
    elif hour >= 12 and hour < 18:
        engine.say("Good Afternoon Sir! how may I help you?")
        engine.runAndWait()
    else:
        engine.say("Good Evening Sir! how may I help you?")
        engine.runAndWait()
