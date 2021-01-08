#!/usr/bin/env python3
import speech_recognition

r = speech_recognition.Recognizer()
with speech_recognition.AudioFile("/tmp/voicemsg.wav") as source:
	audio = r.record(source)
	print(r.recognize_google(audio,language="ru_RU"))
