def TouchVoiceController():
    from gtts import gTTS
    from googletrans import Translator
    from speech_recognition import Microphone, Recognizer, UnknownValueError
    from os import system
    from typing import List, Any

    def mostCommon(lst: List[Any]) -> Any:
        return max(set(lst), key = lst.count)

    r = Recognizer()
    d = False
    langs = ['en']
    currentLang = 'en'
    commonLang = 'en'

    def say(text, lang='en'):
        gTTS(text, lang=lang).save(".firstAudio.mp3")
        system("afplay .firstAudio.mp3")

    def translate(text, dest='en', src='auto'):
        return Translator().translate(text, dest=dest, src=src)

    while not d:
        with Microphone() as source:
            print("Say something..")
            try:
                audio = r.listen(source)
                print("You said: ",r.recognize_google(audio, language=commonLang))
                translated = translate("You said: " + r.recognize_google(audio, language=commonLang), dest='en')
                text = translated.text
                print(text, translated.src)
                text = text.lower()
                if 'forward' in text or 'ahead' in text or 'front' in text:
                    say(translate("I am going forward!").text)
                if 'back' in text:
                    say(translate("I am going backward!").text)
                say(text, translated.src)
                langs.append(translated.src)
                currentLang = translated.src
                commonLang = mostCommon(langs)
                print(langs, currentLang, commonLang)
            except Exception as a:
                raise a
            except UnknownValueError as e:
                pass
    

