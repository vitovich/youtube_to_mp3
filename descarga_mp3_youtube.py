import sys
from pytube import YouTube

# Get the video URL from the program arguments
video_url = sys.argv[1]

# Create a YouTube object and get the video
video = YouTube(video_url)

# Get the highest quality video available
video_stream = video.streams.get_highest_resolution()

# Download the video
video_file = video_stream.download()

# Use ffmpeg to extract the audio from the video file
import subprocess
subprocess.call(['ffmpeg', '-i', video_file,  video.title+'.mp3'])  

# This program uses the pytube library to download YouTube videos in Python, and the ffmpeg command-line tool to extract the audio from the downloaded video file. 
# It gets the URL of the video to download from the program arguments, creates a YouTube object using the URL, and gets the highest quality video available for the specified video. It then downloads the video using the download() method of the VideoStream object, and uses ffmpeg to extract the audio from the video file and save it as an audio.mp3 file.
# To use this program, you will need to install the pytube library and ffmpeg first. You can do this using the following commands:
# # pip install pytube
# On Linux or macOS
# # sudo apt-get install ffmpeg
# On Windows https://www.gyan.dev/ffmpeg/builds/
# # choco install ffmpeg
# Once you have installed the required libraries, you can run the program using the following command:
# # python program.py https://www.youtube.com/watch?v=video_id
# 
# Replace video_id with the ID of the YouTube video that you want to download. This will download the video in the highest quality available and extract the audio from it, 
# saving the audio as an audio.mp3 file in the current working directory. You can adjust the program to specify a different download location, file format, or audio quality.

