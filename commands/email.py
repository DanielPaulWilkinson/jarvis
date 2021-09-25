import webbrowser
import smtplib


def mail(engine):
    engine.speak('On it!')
    webbrowser.open("mail.google.com")
    engine.speak('I\'ve opened a new tab in the browser!')


def send(engine):

    try:
        engine.speak('Who should I send an email to Sir?')
        to = engine.takeCommand()

        engine.speak("What should I say?")
        content = engine.takeCommand()

        sendEmail(to, content)

        engine.speak("Email has been sent!")
    except Exception as e:
        print(e)
        engine.speak("Sorry, I couldn't send the email")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dpw.developer@gmail.com', '1Dan2day2014')
    server.sendmail('dpw.developer@gmail.com', to, content)
    server.close()
