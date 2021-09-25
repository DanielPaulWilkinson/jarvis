import speech
import argument_match


def terminate(query):
    goobyePhrases = ['terminate', 'bye', 'See you', 'cheerio']
    if any(query in goobyePhrases):
        return True


if __name__ == "__main__":
    engine = speech.createSpeechEngine()
    while True:
        # if 1:
        query = speech.takeCommand().lower()
        argument_match.command(engine, query)
