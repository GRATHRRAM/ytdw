import os
from pytube import YouTube
from pytube.cli import on_progress

def download(link, res):
        video = YouTube(link, on_progress_callback=on_progress)

        if res == "0":
            mp3 = video.streams.get_audio_only()
            mp3.download(output_path=".")
            os.rename(mp3.default_filename, mp3.default_filename[0:len(mp3.default_filename) - 3] + "mp3")
        elif res == "1":
            mp4 = video.streams.filter(resolution="144p", progressive=True).first()
            mp4.download(output_path=".")
        elif res == "2":
            mp4 = video.streams.filter(resolution="240p", progressive=True).first()
            mp4.download(output_path=".")
        elif res == "3":
            mp4 = video.streams.filter(resolution="360p", progressive=True).first()
            mp4.download(output_path=".")
        elif res == "5":
            mp4 = video.streams.filter(resolution="480p", progressive=True).first()
            mp4.download(output_path=".")
        elif res == "5":
            mp4 = video.streams.filter(resolution="720p", progressive=True).first()
            mp4.download(output_path=".")
        elif res == "6":
            mp4 = video.streams.get_highest_resolution()
            mp4.download(output_path=".")


link_to_video = input("YOUTUBE Link -> ")
res = input("0 - AUDIO ONLY;\n1 - 144p;\n2 - 240p;\n3 - 360p;\n4 - 480p;\n5 - 720p;\n6 - HIGHEST;\n-> ")
download(link_to_video, res)
