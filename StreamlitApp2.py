import streamlit as st
import logging, sys, os
import whisperAPI as w
import time

#OpenAI Whisper

THIS_FOLDER = os.path.join(os.path.dirname(__file__))
AUDIO_FOLDER = THIS_FOLDER + "\\audioFiles\\"

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

st.title("Whisper AI audio transcriber :sunglasses:")


"""
TO DO:
Load in audio into a variable so I don't have to use file path
"""

model = w.load_model("tiny") #Pre-set model - Remove this when better method of avoiding is found

st.markdown("## Audio File")

#Read all files in audio folder

audio_files = [f for f in os.listdir(AUDIO_FOLDER) if os.path.isfile(os.path.join(AUDIO_FOLDER, f))]
#Ensure only valid file types make it through
print(audio_files)

selected_audio_files = st.multiselect("Select audio files to be transcribed", audio_files)

selected_model = st.radio("Choose a model", ["tiny", "base", "small", "medium", "large"], horizontal=True, index=3)

load_model_button = st.button("Load " + selected_model + " model")

transcribe_audio_button = st.button("Transcribe audio")

transcribed_text_placeholder = st.empty()

if selected_audio_files:
    logging.info(str(selected_audio_files) + " audio files selected")

if selected_model:
    logging.info(selected_model + " model selected")

if load_model_button:
    model = w.load_model(selected_model)

if transcribe_audio_button:
    for audio_file in selected_audio_files:
        audio_file_path = AUDIO_FOLDER + audio_file
        
        start_time = time.time()
        transcribed_text = w.transcribe_audio(model, audio_file_path)["text"]
        end_time = time.time()

        print(audio_file + "Transcribed in " + str(end_time - start_time))

        st.markdown("### " + audio_file)
        st.write(transcribed_text)

    
