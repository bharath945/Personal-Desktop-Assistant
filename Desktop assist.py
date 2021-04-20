import pyttsx3
import datetime
import speech_recognition as sr
import time
import wikipedia
import webbrowser
engine=pyttsx3.init()
r=sr.Recognizer()
def listen():
    sa=''
    with sr.Microphone() as source:
        print()
        print('Listening....')
        data=r.listen(source)
        try:
            print()
            print('Recognizing....')
            sa=r.recognize_google(data)
        except:
            speek('naku ardam kaledu ra malla matladu')
            listen()
    return sa
def speek(data):
    print()
    print(data)
    engine.say(data)
    engine.runAndWait()
def wish():
    h=int(datetime.datetime.now().hour)
    #print(h)
    if h>=0 and h<12:
        speek('hi i am you tommy,good morning sir,how can i help you')
    elif h<=16:
        speek('hi i am you tommy,good afternoon sir,how can i help you')
    elif h<=21:
        speek('hi i am you tommy,good evening sir,how can i help you')
    else:
        speek('hi i am you tommy,good night sir,how can i help you')
if __name__ == "__main__":
    wish()
    while True:
        speek('press any key to talk')
        input()
        a=listen().lower()
        print(a)
        if 'tommay' in a:
            print(a)
        if 'hi' in a:
            speek('hi sir')
        elif 'how are you' in a:
            speek('i am good i hope you are good')
        else:
            #print('i am good i hope you are good')
            if ('who' in a) and (('made' in a) or ('create' in a)) and ('you' in a):
                speek('mr.VENIGALLA SAI BHARATH has created me')
            elif 'are you' in a:
                speek('i am tommy your assits')
            elif 'your name' in a:
                speek('my name is tommy')
            elif 'open youtube' in a:
                webbrowser.open('youtube.com')
            elif 'open google' in a:
                webbrowser.open('google.com')
            elif 'open gamil' in a or 'open email' in a:
                webbrowser.open('gmail.com')
            elif 'open codeforces' in a:
                webbrowser.open('codeforces.com')
            elif 'open codechef' in a:
                webbrowser.open('codechef.com')
            elif 'open hackerrank' in a:
                webbrowser.open('hackerrank.com')
            elif 'open' in a:
                speek('please tell only web site address')
                a=listen()
                print(a)
                webbrowser.open(a)
            elif ('bye' in a) or ('quit' in a):
                speek('bye sir have a nice day')
                print('bye sir have a nice day')
                break
            else:
                try:
                    result=wikipedia.summary(a,sentences=1)
                    speek('according to wikipedia')
                    speek(result)
                    speek('for more information press y else n:')
                    s=input().lower()
                    if s=='y':
                        webbrowser.open(a)
                    else:
                        pass
                except:
                    webbrowser.open(a)
