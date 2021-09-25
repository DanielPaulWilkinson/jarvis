import commands


def command(engine, query):
    if "jarvis" and "wake" in query:
        commands.launch(engine)
    elif "jarvis" and "wikipedia" in query:
        commands.search(engine, query)
    # Socials
    elif "jarvis" and "socials" in query:
        commands.openSocials(engine)
    elif "jarvis" and "facebook" in query:
        commands.openFacebook(engine)
    elif "jarvis" and "twitter" in query:
        commands.openTwitter(engine)
    elif "jarvis" and "instagram" in query:
        commands.openInstagram(engine)
    elif "jarvis" and "linkedin" in query:
        commands.openLinkedIn(engine)
    elif "jarvis" and "amazon" in query:
        commands.openAmazion(engine)
    elif "jarvis" and "netflix" in query:
        commands.openNetflix(engine)
    elif "jarvis" and "reddit" in query:
        commands.openRReddit(engine)
    # Programms
    elif "jarvis" and "code" in query:
        commands.OpenProgramVisualStudioCode()
    elif "jarvis" and "visual studio" in query:
        commands.openVisualStudio()
    elif "jarvis" and "postman" in query:
        commands.OpenPostMan()
    elif "jarvis" and "android studio" in query:
        commands.launchAndroidStudio()
    elif "jarvis" and "whatsapp" in query:
        commands.OpenWhatsApp()
    elif "jarvis" and "minecraft" in query:
        commands.launchMinecraft()
    elif "jarvis" and "steam" in query:
        commands.launchSteam()
    # volume
    elif "jarvis" and "volume" and "100" in query:
        commands.volume100()
    elif "jarvis" and "volume" and "90" in query:
        commands.volume90()
    elif "jarvis" and "volume" and "80" in query:
        commands.volume80()
    elif "jarvis" and "volume" and "70" in query:
        commands.volume70()
    elif "jarvis" and "volume" and "60" in query:
        commands.volume60()
    elif "jarvis" and "volume" and "50" in query:
        commands.volume50()
    elif "jarvis" and "volume" and "40" in query:
        commands.volume40()
    elif "jarvis" and "volume" and "30" in query:
        commands.volume30()
    elif "jarvis" and "volume" and "20" in query:
        commands.volume20()
    elif "jarvis" and "volume" and "10" in query:
        commands.volume10()
    elif "jarvis" and "volume" and "0" or "jarvis" and "mute" in query:
        commands.volume0()
    # pc actions
    elif "shutdown":
        commands.shutdown()
    # time
    elif "jarvis" and "time" in query:
        commands.time(engine)
