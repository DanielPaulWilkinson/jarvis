import datetime


def time(engine):
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    engine.speak(f"Sir, the time is {strTime}")

