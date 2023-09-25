import streamlit as st
from streamlit_audio_recorder import AudioRecorder

def app():
    st.set_page_config(page_title="Audio Recorder", page_icon="🎤")

    st.write("# Record Audio in Streamlit")
    audio_recorder = AudioRecorder()
    audio_file = audio_recorder()

    if audio_file:
        st.audio(audio_file, format="audio/wav")

if __name__ == "__main__":
    app()
