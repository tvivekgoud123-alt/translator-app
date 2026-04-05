import streamlit as st
from googletrans import Translator
from gtts import gTTS

translator = Translator()

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta"
}

st.title("🌐 Translator App")

text = st.text_area("Enter text")

from_lang = st.selectbox("From", list(languages.keys()))
to_lang = st.selectbox("To", list(languages.keys()))

if st.button("Translate"):
    if text:
        result = translator.translate(
            text,
            src=languages[from_lang],
            dest=languages[to_lang]
        )

        st.success(result.text)

        tts = gTTS(result.text, lang=languages[to_lang])
        tts.save("audio.mp3")

        st.audio("audio.mp3")
    else:
        st.error("Enter text first")
        