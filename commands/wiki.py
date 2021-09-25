import wikipedia


def search(engine, query):
    print(query)
    engine.say('Searching Wikipedia...')
    engine.runAndWait()
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=10)
    engine.say("According to Wikipedia")
    engine.runAndWait()
    engine.say(results)
    engine.runAndWait()
