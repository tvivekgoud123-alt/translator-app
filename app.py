!pip install speechrecognition
!pip install googletrans==4.0.0-rc1
!pip install gtts
!pip install playsound

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import messagebox

# Initialize
recog = sr.Recognizer()
translator = Translator()

# Language mapping (name → code)
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de"
}

# ---------- TEXT TRANSLATION ----------
def translate_text():
    try:
        text = input_text_var.get()
        if text == "":
            messagebox.showerror("Error", "Enter text")
            return

        src = language_codes[from_lang.get()]
        dest = language_codes[to_lang.get()]

        translated = translator.translate(text, src=src, dest=dest)

        output_text.set(translated.text)

        # Speech
        tts = gTTS(translated.text, lang=dest)
        tts.save("output.mp3")
        playsound("output.mp3")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- VOICE TRANSLATION ----------
def translate_voice():
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            audio = recog.listen(source)

        text = recog.recognize_google(audio)
        input_text_var.set(text)

        src = language_codes[from_lang.get()]
        dest = language_codes[to_lang.get()]

        translated = translator.translate(text, src=src, dest=dest)

        output_text.set(translated.text)

        tts = gTTS(translated.text, lang=dest)
        tts.save("output.mp3")
        playsound("output.mp3")

        status_label.config(text="Done")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- GUI ----------
root = tk.Tk()
root.title("Translator App")
root.geometry("500x400")

input_text_var = tk.StringVar()
output_text = tk.StringVar()

from_lang = tk.StringVar(value="English")
to_lang = tk.StringVar(value="Telugu")

# Input
tk.Label(root, text="Enter Text").pack()
tk.Entry(root, textvariable=input_text_var, width=40).pack()

# Output
tk.Label(root, text="Translated").pack()
tk.Entry(root, textvariable=output_text, width=40, state="readonly").pack()

# Language
tk.Label(root, text="From").pack()
tk.OptionMenu(root, from_lang, *language_codes.keys()).pack()

tk.Label(root, text="To").pack()
tk.OptionMenu(root, to_lang, *language_codes.keys()).pack()

# Buttons
tk.Button(root, text="Translate Text", command=translate_text).pack(pady=10)
tk.Button(root, text="Translate Voice", command=translate_voice).pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
