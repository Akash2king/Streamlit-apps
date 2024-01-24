import streamlit as st
from pytube import YouTube
import os
import shutil as S

def download_video(link, path, resolution_choice):
    yt = YouTube(link)
    
    if resolution_choice == 5:
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download("/storage/emulated/0/Download")
        S.move(os.path.join(path, yt.title + ".mp4"), os.path.join(path, yt.title + ".mp3"))
        st.success("Audio Download Completed!")
        return

    if resolution_choice == 1:
        video_stream = yt.streams.get_highest_resolution()
    elif resolution_choice == 2:
        video_stream = yt.streams.get_by_resolution("720p")
    elif resolution_choice == 3:
        video_stream = yt.streams.get_by_resolution("480p")
    elif resolution_choice == 4:
        video_stream = yt.streams.get_by_resolution("360p")
    else:
        st.error("Invalid choice")
        return

    video_stream.download(path)
    st.success("Video Download Completed!")

# Streamlit UI
st.title("YouTube Video Downloader")

link = st.text_input("Enter YouTube link:")
path = st.text_input("Enter the path you want to save:")
resolution_choice = st.selectbox("Select resolution for video download:", ["Highest Resolution", "720p", "480p", "360p", "Audio only"])

if st.button("Download"):
    if link and path:
        resolution_mapping = {"Highest Resolution": 1, "720p": 2, "480p": 3, "360p": 4, "Audio only": 5}
        resolution_code = resolution_mapping[resolution_choice]
        download_video(link, path, resolution_code)
    else:
        st.warning("Please enter both YouTube link and path before downloading.")
