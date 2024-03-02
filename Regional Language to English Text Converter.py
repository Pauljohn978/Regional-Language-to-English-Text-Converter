import streamlit as st
import speech_recognition as sr

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = "Unable to transcribe audio. Please try again."
    return text

def main():
    st.title("Malayalam Audio to English Text Converter")
    uploaded_file = st.file_uploader("Upload an audio file (.wav, .mp3)", type=["wav", "mp3"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav', start_time=0)
        if st.button("Transcribe"):
            text = transcribe_audio(uploaded_file)
            st.write("Transcribed Text:")
            st.write(text)

if __name__ == "__main__":
    main()

